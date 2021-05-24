#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File        :   yolov3_helper.py
@Path        :   agrothon/server/helpers/
@Time        :   2021/05/5
@Author      :   github.com/zzh8829
@Modifed by  :   Chandra Kiran Viswanath Balusu
@Version     :   1.2.6
@Contact     :   ckvbalusu@gmail.com
@Desc        :   Yolov3 Python3 Wrapper using tf2
"""

import logging
import os
from pathlib import Path
from typing import List, Optional, Tuple

import cv2
import numpy as np
import tensorflow as tf
from PIL import Image, ImageDraw, ImageFont
from seaborn import color_palette
from tensorflow.keras import Model
from tensorflow.keras.layers import (
    Add,
    BatchNormalization,
    Concatenate,
    Conv2D,
    Input,
    Lambda,
    LeakyReLU,
    UpSampling2D,
    ZeroPadding2D,
)
from tensorflow.keras.regularizers import l2

tf.get_logger().setLevel("ERROR")
tf.autograph.set_verbosity(3)

LOGGER = logging.getLogger(__name__)
yolo_max_boxes = 100  # maximum number of boxes per image
yolo_iou_threshold = 0.5  # iou threshold
yolo_score_threshold = 0.5  # score threshold
yolo_anchors = (
    np.array(
        [
            (10, 13),
            (16, 30),
            (33, 23),
            (30, 61),
            (62, 45),
            (59, 119),
            (116, 90),
            (156, 198),
            (373, 326),
        ],
        np.float32,
    )
    / 416
)
yolo_anchor_masks = np.array([[6, 7, 8], [3, 4, 5], [0, 1, 2]])

YOLOV3_LAYER_LIST = [
    "yolo_darknet",
    "yolo_conv_0",
    "yolo_output_0",
    "yolo_conv_1",
    "yolo_output_1",
    "yolo_conv_2",
    "yolo_output_2",
]

""" --------------------------------Models------------------------------ """


def DarknetConv(x, filters, size, strides=1, batch_norm=True):
    if strides == 1:
        padding = "same"
    else:
        x = ZeroPadding2D(((1, 0), (1, 0)))(x)
        padding = "valid"
    x = Conv2D(
        filters=filters,
        kernel_size=size,
        strides=strides,
        padding=padding,
        use_bias=not batch_norm,
        kernel_regularizer=l2(0.0005),
    )(x)
    if batch_norm:
        x = BatchNormalization()(x)
        x = LeakyReLU(alpha=0.1)(x)
    return x


def DarknetResidual(x, filters):
    prev = x
    x = DarknetConv(x, filters // 2, 1)
    x = DarknetConv(x, filters, 3)
    x = Add()([prev, x])
    return x


def DarknetBlock(x, filters, blocks):
    x = DarknetConv(x, filters, 3, strides=2)
    for _ in range(blocks):
        x = DarknetResidual(x, filters)
    return x


def Darknet(name=None):
    x = inputs = Input([None, None, 3])
    x = DarknetConv(x, 32, 3)
    x = DarknetBlock(x, 64, 1)
    x = DarknetBlock(x, 128, 2)
    x = x_36 = DarknetBlock(x, 256, 8)
    x = x_61 = DarknetBlock(x, 512, 8)
    x = DarknetBlock(x, 1024, 4)
    return tf.keras.Model(inputs, (x_36, x_61, x), name=name)


def YoloConv(filters, name=None):
    def yolo_conv(x_in):
        if isinstance(x_in, tuple):
            inputs = Input(x_in[0].shape[1:]), Input(x_in[1].shape[1:])
            x, x_skip = inputs
            x = DarknetConv(x, filters, 1)
            x = UpSampling2D(2)(x)
            x = Concatenate()([x, x_skip])
        else:
            x = inputs = Input(x_in.shape[1:])

        x = DarknetConv(x, filters, 1)
        x = DarknetConv(x, filters * 2, 3)
        x = DarknetConv(x, filters, 1)
        x = DarknetConv(x, filters * 2, 3)
        x = DarknetConv(x, filters, 1)
        return Model(inputs, x, name=name)(x_in)

    return yolo_conv


def YoloOutput(filters, anchors, classes, name=None):
    def yolo_output(x_in):
        x = inputs = Input(x_in.shape[1:])
        x = DarknetConv(x, filters * 2, 3)
        x = DarknetConv(x, anchors * (classes + 5), 1, batch_norm=False)
        x = Lambda(
            lambda x: tf.reshape(
                x, (-1, tf.shape(x)[1], tf.shape(x)[2], anchors, classes + 5)
            )
        )(x)
        return tf.keras.Model(inputs, x, name=name)(x_in)

    return yolo_output


def _meshgrid(n_a, n_b):
    return [
        tf.reshape(tf.tile(tf.range(n_a), [n_b]), (n_b, n_a)),
        tf.reshape(tf.repeat(tf.range(n_b), n_a), (n_b, n_a)),
    ]


def yolo_boxes(pred, anchors, classes):
    grid_size = tf.shape(pred)[1:3]
    box_xy, box_wh, objectness, class_probs = tf.split(
        pred, (2, 2, 1, classes), axis=-1
    )

    box_xy = tf.sigmoid(box_xy)
    objectness = tf.sigmoid(objectness)
    class_probs = tf.sigmoid(class_probs)
    pred_box = tf.concat((box_xy, box_wh), axis=-1)

    grid = _meshgrid(grid_size[1], grid_size[0])
    grid = tf.expand_dims(tf.stack(grid, axis=-1), axis=2)

    box_xy = (box_xy + tf.cast(grid, tf.float32)) / tf.cast(grid_size, tf.float32)
    box_wh = tf.exp(box_wh) * anchors

    box_x1y1 = box_xy - box_wh / 2
    box_x2y2 = box_xy + box_wh / 2
    bbox = tf.concat([box_x1y1, box_x2y2], axis=-1)

    return bbox, objectness, class_probs, pred_box


def yolo_nms(outputs, anchors, masks, classes):
    b, c, t = [], [], []

    for o in outputs:
        b.append(tf.reshape(o[0], (tf.shape(o[0])[0], -1, tf.shape(o[0])[-1])))
        c.append(tf.reshape(o[1], (tf.shape(o[1])[0], -1, tf.shape(o[1])[-1])))
        t.append(tf.reshape(o[2], (tf.shape(o[2])[0], -1, tf.shape(o[2])[-1])))

    bbox = tf.concat(b, axis=1)
    confidence = tf.concat(c, axis=1)
    class_probs = tf.concat(t, axis=1)

    scores = confidence * class_probs

    dscores = tf.squeeze(scores, axis=0)
    scores = tf.reduce_max(dscores, [1])
    bbox = tf.reshape(bbox, (-1, 4))
    classes = tf.argmax(dscores, 1)
    selected_indices, selected_scores = tf.image.non_max_suppression_with_scores(
        boxes=bbox,
        scores=scores,
        max_output_size=yolo_max_boxes,
        iou_threshold=yolo_iou_threshold,
        score_threshold=yolo_score_threshold,
        soft_nms_sigma=0.5,
    )

    num_valid_nms_boxes = tf.shape(selected_indices)[0]

    selected_indices = tf.concat(
        [selected_indices, tf.zeros(yolo_max_boxes - num_valid_nms_boxes, tf.int32)], 0
    )
    selected_scores = tf.concat(
        [selected_scores, tf.zeros(yolo_max_boxes - num_valid_nms_boxes, tf.float32)],
        -1,
    )

    boxes = tf.gather(bbox, selected_indices)
    boxes = tf.expand_dims(boxes, axis=0)
    scores = selected_scores
    scores = tf.expand_dims(scores, axis=0)
    classes = tf.gather(classes, selected_indices)
    classes = tf.expand_dims(classes, axis=0)
    valid_detections = num_valid_nms_boxes
    valid_detections = tf.expand_dims(valid_detections, axis=0)

    return boxes, scores, classes, valid_detections


def YoloV3(
    size=None,
    channels=3,
    anchors=yolo_anchors,
    masks=yolo_anchor_masks,
    classes=80,
    training=False,
):
    x = inputs = Input([size, size, channels], name="input")

    x_36, x_61, x = Darknet(name="yolo_darknet")(x)

    x = YoloConv(512, name="yolo_conv_0")(x)
    output_0 = YoloOutput(512, len(masks[0]), classes, name="yolo_output_0")(x)

    x = YoloConv(256, name="yolo_conv_1")((x, x_61))
    output_1 = YoloOutput(256, len(masks[1]), classes, name="yolo_output_1")(x)

    x = YoloConv(128, name="yolo_conv_2")((x, x_36))
    output_2 = YoloOutput(128, len(masks[2]), classes, name="yolo_output_2")(x)

    if training:
        return Model(inputs, (output_0, output_1, output_2), name="yolov3")

    boxes_0 = Lambda(
        lambda x: yolo_boxes(x, anchors[masks[0]], classes), name="yolo_boxes_0"
    )(output_0)
    boxes_1 = Lambda(
        lambda x: yolo_boxes(x, anchors[masks[1]], classes), name="yolo_boxes_1"
    )(output_1)
    boxes_2 = Lambda(
        lambda x: yolo_boxes(x, anchors[masks[2]], classes), name="yolo_boxes_2"
    )(output_2)

    outputs = Lambda(lambda x: yolo_nms(x, anchors, masks, classes), name="yolo_nms")(
        (boxes_0[:3], boxes_1[:3], boxes_2[:3])
    )

    return Model(inputs, outputs, name="yolov3")


""" --------------------------------Data Set Utils------------------------------ """


@tf.function
def transform_targets_for_output(y_true, grid_size, anchor_idxs):
    N = tf.shape(y_true)[0]
    y_true_out = tf.zeros((N, grid_size, grid_size, tf.shape(anchor_idxs)[0], 6))

    anchor_idxs = tf.cast(anchor_idxs, tf.int32)

    indexes = tf.TensorArray(tf.int32, 1, dynamic_size=True)
    updates = tf.TensorArray(tf.float32, 1, dynamic_size=True)
    idx = 0
    for i in tf.range(N):
        for j in tf.range(tf.shape(y_true)[1]):
            if tf.equal(y_true[i][j][2], 0):
                continue
            anchor_eq = tf.equal(anchor_idxs, tf.cast(y_true[i][j][5], tf.int32))

            if tf.reduce_any(anchor_eq):
                box = y_true[i][j][0:4]
                box_xy = (y_true[i][j][0:2] + y_true[i][j][2:4]) / 2

                anchor_idx = tf.cast(tf.where(anchor_eq), tf.int32)
                grid_xy = tf.cast(box_xy // (1 / grid_size), tf.int32)

                indexes = indexes.write(
                    idx, [i, grid_xy[1], grid_xy[0], anchor_idx[0][0]]
                )
                updates = updates.write(
                    idx, [box[0], box[1], box[2], box[3], 1, y_true[i][j][4]]
                )
                idx += 1

    return tf.tensor_scatter_nd_update(y_true_out, indexes.stack(), updates.stack())


def transform_targets(y_train, anchors, anchor_masks, size):
    y_outs = []
    grid_size = size // 32
    anchors = tf.cast(anchors, tf.float32)
    anchor_area = anchors[..., 0] * anchors[..., 1]
    box_wh = y_train[..., 2:4] - y_train[..., 0:2]
    box_wh = tf.tile(tf.expand_dims(box_wh, -2), (1, 1, tf.shape(anchors)[0], 1))
    box_area = box_wh[..., 0] * box_wh[..., 1]
    intersection = tf.minimum(box_wh[..., 0], anchors[..., 0]) * tf.minimum(
        box_wh[..., 1], anchors[..., 1]
    )
    iou = intersection / (box_area + anchor_area - intersection)
    anchor_idx = tf.cast(tf.argmax(iou, axis=-1), tf.float32)
    anchor_idx = tf.expand_dims(anchor_idx, axis=-1)

    y_train = tf.concat([y_train, anchor_idx], axis=-1)

    for anchor_idxs in anchor_masks:
        y_outs.append(transform_targets_for_output(y_train, grid_size, anchor_idxs))
        grid_size *= 2

    return tuple(y_outs)


def transform_images(x_train, size):
    x_train = tf.image.resize(x_train, (size, size))
    x_train = x_train / 255
    return x_train


IMAGE_FEATURE_MAP = {
    "image/encoded": tf.io.FixedLenFeature([], tf.string),
    "image/object/bbox/xmin": tf.io.VarLenFeature(tf.float32),
    "image/object/bbox/ymin": tf.io.VarLenFeature(tf.float32),
    "image/object/bbox/xmax": tf.io.VarLenFeature(tf.float32),
    "image/object/bbox/ymax": tf.io.VarLenFeature(tf.float32),
    "image/object/class/text": tf.io.VarLenFeature(tf.string),
}


def parse_tfrecord(tfrecord, class_table, size):
    x = tf.io.parse_single_example(tfrecord, IMAGE_FEATURE_MAP)
    x_train = tf.image.decode_jpeg(x["image/encoded"], channels=3)
    x_train = tf.image.resize(x_train, (size, size))

    class_text = tf.sparse.to_dense(x["image/object/class/text"], default_value="")
    labels = tf.cast(class_table.lookup(class_text), tf.float32)
    y_train = tf.stack(
        [
            tf.sparse.to_dense(x["image/object/bbox/xmin"]),
            tf.sparse.to_dense(x["image/object/bbox/ymin"]),
            tf.sparse.to_dense(x["image/object/bbox/xmax"]),
            tf.sparse.to_dense(x["image/object/bbox/ymax"]),
            labels,
        ],
        axis=1,
    )

    paddings = [[0, yolo_max_boxes - tf.shape(y_train)[0]], [0, 0]]
    y_train = tf.pad(y_train, paddings)

    return x_train, y_train


""" --------------------------------Utils------------------------------ """


def load_darknet_weights(model, weights_file):
    wf = open(weights_file, "rb")
    major, minor, revision, seen, _ = np.fromfile(wf, dtype=np.int32, count=5)

    layers = YOLOV3_LAYER_LIST

    for layer_name in layers:
        sub_model = model.get_layer(layer_name)
        for i, layer in enumerate(sub_model.layers):
            if not layer.name.startswith("conv2d"):
                continue
            batch_norm = None
            if i + 1 < len(sub_model.layers) and sub_model.layers[
                i + 1
            ].name.startswith("batch_norm"):
                batch_norm = sub_model.layers[i + 1]

            logging.info(
                "{}/{} {}".format(
                    sub_model.name, layer.name, "bn" if batch_norm else "bias"
                )
            )

            filters = layer.filters
            size = layer.kernel_size[0]
            in_dim = layer.get_input_shape_at(0)[-1]

            if batch_norm is None:
                conv_bias = np.fromfile(wf, dtype=np.float32, count=filters)
            else:
                bn_weights = np.fromfile(wf, dtype=np.float32, count=4 * filters)
                bn_weights = bn_weights.reshape((4, filters))[[1, 0, 2, 3]]

            conv_shape = (filters, in_dim, size, size)
            conv_weights = np.fromfile(
                wf, dtype=np.float32, count=np.product(conv_shape)
            )
            conv_weights = conv_weights.reshape(conv_shape).transpose([2, 3, 1, 0])

            if batch_norm is None:
                layer.set_weights([conv_weights, conv_bias])
            else:
                layer.set_weights([conv_weights])
                batch_norm.set_weights(bn_weights)

    assert len(wf.read()) == 0, "failed to read all data"
    wf.close()


def draw_outputs(img, outputs, class_names):
    colors = (np.array(color_palette("hls", 80)) * 255).astype(np.uint8)
    boxes, objectness, classes, nums = outputs
    wh = np.flip(img.shape[0:2])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(
        font="./data/fonts/futur.ttf", size=(img.size[0] + img.size[1]) // 100
    )
    for i in range(nums):
        color = colors[int(classes[i])]
        x1y1 = (np.array(boxes[i][0:2]) * wh).astype(np.int32)
        x2y2 = (np.array(boxes[i][2:4]) * wh).astype(np.int32)
        thickness = (img.size[0] + img.size[1]) // 200
        x0, y0 = x1y1[0], x1y1[1]
        for t in np.linspace(0, 1, thickness):
            x1y1[0], x1y1[1] = x1y1[0] - t, x1y1[1] - t
            x2y2[0], x2y2[1] = x2y2[0] - t, x2y2[1] - t
            draw.rectangle([x1y1[0], x1y1[1], x2y2[0], x2y2[1]], outline=tuple(color))
        confidence = "{:.2f}%".format(objectness[i] * 100)
        text = "{} {}".format(class_names[int(classes[i])], confidence)
        text_size = draw.textsize(text, font=font)
        draw.rectangle(
            [x0, y0 - text_size[1], x0 + text_size[0], y0], fill=tuple(color)
        )
        draw.text((x0, y0 - text_size[1]), text, fill="black", font=font)
    rgb_img = img.convert("RGB")
    img_np = np.asarray(rgb_img)
    img = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    return img


""" --------------------------------Methods to Detect image goes here------------------------------ """

_yolo = YoloV3(classes=80)
gen_exist = False
try:
    paths = []
    for path in Path("data/models/yolo/weights/").glob("yolov3.tf*"):
        paths.append(path)
    if len(paths) == 2:
        gen_exist = True
        raise FileExistsError
except FileExistsError:
    _yolo.load_weights("data/models/yolo/weights/yolov3.tf").expect_partial()
    LOGGER.info("Loaded Generated Weights")

try:
    if not gen_exist:
        if os.path.exists("data/models/yolo/yolov3.weights"):
            load_darknet_weights(_yolo, "data/models/yolo/yolov3.weights")
            LOGGER.info("Loaded Yolov3 Weights")
            _yolo.save_weights("data/models/yolo/weights/yolov3.tf")
            LOGGER.info("Saved Yolov3 Weights")
            _yolo.load_weights("data/models/yolo/weights/yolov3.tf").expect_partial()
            LOGGER.info("Loaded Generated Weights")
        else:
            raise FileNotFoundError
except FileNotFoundError:
    LOGGER.error("Neither Generated weights or yolov3.weights not found")
    exit(1)
try:
    if os.path.exists("data/models/yolo/coco.names"):
        _class_names = [
            c.strip() for c in open("data/models/yolo/coco.names").readlines()
        ]
        LOGGER.info("Loaded classes from coco.names")
    else:
        raise FileNotFoundError
except FileNotFoundError:
    LOGGER.error(f"Coco.names not found :(")
    exit(1)


# INCLUDED_CLASSES = ["person", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe"]
INC_CLASS_NUMBERS = [0, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

def yolo_detect(
    _image: bytes,
    filter: bool = True,
) -> Tuple[
    Optional[bool],
    Optional[int],
    Optional[List],
    Optional[int],
    Optional[bool],
    Optional[bytes],
]:
    try:
        LOGGER.info("Started detection of Objects in the image")
        img_raw = tf.image.decode_image(_image, channels=3)
        _img_ = tf.expand_dims(img_raw, 0)
        img__ = transform_images(_img_, 416)
        _boxes, _scores, _classes, _nums = _yolo(img__)
        filtered_boxes, filtered_scores, filtered_classes, new_nums = [], [], [], 0
        if filter:
            for i in range(_nums[0]):
                if int(_classes[0][i]) in INC_CLASS_NUMBERS:
                    filtered_classes.append(int(_classes[0][i]))
                    filtered_boxes.append(_boxes[0][i])
                    filtered_scores.append(_scores[0][i])
                    new_nums += 1
        else:
            filtered_classes = _classes[0]
            filtered_boxes = _boxes[0]
            filtered_scores = _scores[0]
            new_nums = _nums[0]

        if new_nums > 0:
            detections_list = []
            humans = 0
            only_humans = False
            _objects = {}
            _confidences = {}
            for i in range(new_nums):
                if str(_class_names[filtered_classes[i]]) in _objects:

                    _objects[str(_class_names[filtered_classes[i]])] += 1
                    _confidences[str(_class_names[filtered_classes[i]])].append(
                        round(float(np.array(filtered_scores[i])) * 100, 2)
                    )
                else:
                    _objects[str(_class_names[filtered_classes[i]])] = 1
                    _confidences[str(_class_names[filtered_classes[i]])] = [
                        round(float(np.array(filtered_scores[i])) * 100, 2)
                    ]

                if (_class_names[int(filtered_classes[i])]) == "person":
                    humans += 1
            for i in _objects:
                detection_dict = {
                    "type": i,
                    "confidences": _confidences[i],
                    "count": _objects[i],
                }
                detections_list.append(detection_dict)

            if _nums[0] == humans:
                only_humans = True
            cv2_img = cv2.cvtColor(img_raw.numpy(), cv2.COLOR_RGB2BGR)
            cv2_img = draw_outputs(
                cv2_img, (filtered_boxes, filtered_scores, filtered_classes, new_nums), _class_names
            )
            is_success, cv2_img = cv2.imencode(".jpg", cv2_img)
            LOGGER.debug(f"Finished Detecting, Objects found : {str(detections_list)}")
            return True, int(new_nums), detections_list, humans, only_humans, cv2_img
        else:
            LOGGER.debug(f"Finished Detecting, Nothing Found in the image")
            return False, None, None, None, None, None
    except Exception as e:
        LOGGER.error(f"Error occurred while predicting : {str(e)}")
        return None, None, None, None, None, None
