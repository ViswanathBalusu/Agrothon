#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   intruder.py
@Path    :   agrothon/server/routers/
@Time    :   2021/05/24
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.2.7
@Contact :   ckvbalusu@gmail.com
@Desc    :   Intruder Image Detection Router using Yolov3
"""

import base64
import io
import logging
import uuid
from datetime import datetime
from uuid import UUID

import orjson
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
from starlette.responses import StreamingResponse

from agrothon import MDBClient

from ..helpers.response_models import (
    ImageSuccessResponse,
    ImageUUID,
    IntruderInstantResponse,
)
from ..helpers.yolov3_helper import yolo_detect

LOGGER = logging.getLogger(__name__)

IntruderRouter = APIRouter(
    prefix="/intruder",
    tags=["Intruder Detection"],
    responses={404: {"error": "Not found"}},
)


@IntruderRouter.post(
    "/detect/instant",
    response_class=ORJSONResponse,
    response_model=IntruderInstantResponse,
)
async def image_instant_detect_post(image: UploadFile = File(...)):
    image_cont = await image.read()
    _db = await MDBClient.get_db()
    _intruder_instant = _db["instant_detect"]
    n_docs = await _intruder_instant.estimated_document_count()
    status, nos, det_list, _hum, _only_hum, _img = yolo_detect(image_cont, filter=False)
    if status is not None:
        if status:
            _uuid = str(uuid.uuid4())
            b64_image_string = base64.b64encode(_img)
            await _intruder_instant.update_one(
                {"_id": n_docs},
                {"$set": {"uuid": _uuid, "image": b64_image_string}},
                upsert=True,
            )
            LOGGER.info(f"Saved an image in database with UUID {_uuid}")
            detections_dict = {
                "uuid": _uuid,
                "detections": det_list,
                "no_of_detections": nos,
                "humans": _hum,
                "only_humans": _only_hum,
            }
            LOGGER.debug(
                f"Instant Image Detection Response : {orjson.dumps(detections_dict)}"
            )
            return ORJSONResponse(content=detections_dict)
        else:
            LOGGER.warning("Nothing found in the image")
            raise HTTPException(
                status_code=420, detail={"Error": "Nothing found in image"}
            )
    else:
        LOGGER.error(f"Something wrong happened with Yolov3")
        raise HTTPException(
            status_code=404, detail={"Error": "Error occoured, try again"}
        )


@IntruderRouter.get("/detect/instant/{image_uuid}", response_class=StreamingResponse)
async def image_instant_get(image_uuid: UUID):
    """
    - **image_uuid** : Unique UUID to Search image in Database
    * Response will be the Image
        * Once the image is fetched it will be deleted from the database

    """
    _db = await MDBClient.get_db()
    _intruder_instant = _db["instant_detect"]
    try:
        LOGGER.info(f"Searching in Database for the IMage with UUID {image_uuid}")
        data = await _intruder_instant.find_one_and_delete({"uuid": str(image_uuid)})
        image = base64.b64decode(data["image"])
        return StreamingResponse(io.BytesIO(image), media_type="image/jpeg")
    except TypeError as e:
        LOGGER.warning(f"Image not found in the database : Error: {e}")
        raise HTTPException(
            status_code=404,
            detail={"status": f"Image UUID {image_uuid} not found in the DB"},
        )


@IntruderRouter.post(
    "/detect", response_class=ORJSONResponse, response_model=ImageSuccessResponse
)
async def image_post(image: UploadFile = File(...)):
    """
    - **Post an image*
    - **image** : Image
    - This image will be analyzed for intruders and returns uuid of image
    - if Nothing is found error 420 is returned

    """
    _db = await MDBClient.get_db()
    _intruder = _db["intruder"]
    _intruder_images = _db["images"]
    now = datetime.now()
    time_date = now.strftime("%X %x")
    image_cont = await image.read()
    status, nos, det_list, _hum, _only_hum, _img = yolo_detect(image_cont)
    n_docs = await _intruder.estimated_document_count()
    if status is not None:
        if status:
            _uuid = str(uuid.uuid4())
            b64_image_string = base64.b64encode(_img)
            detections_dict = {
                "uuid": _uuid,
                "detections": det_list,
                "no_of_detections": nos,
                "humans": _hum,
                "only_humans": _only_hum,
                "at": time_date,
            }
            image_dict = {"uuid": _uuid, "image": b64_image_string}
            await _intruder.update_one(
                {"_id": n_docs}, {"$set": detections_dict}, upsert=True
            )
            await _intruder_images.update_one(
                {"_id": n_docs}, {"$set": image_dict}, upsert=True
            )
            LOGGER.info(f"Saved an image in database with UUID {_uuid}")
            j_resp = {"Detected_Intruders": True, "image_uuid": _uuid}
            LOGGER.debug(f"no of intruders detected: {str(nos)}")
            return ORJSONResponse(content=j_resp)
        else:
            LOGGER.warning("Nothing found in the image")
            raise HTTPException(
                status_code=420, detail={"Error": "Nothing found in image"}
            )
    else:
        LOGGER.error(f"Something wrong happened with Yolov3")
        raise HTTPException(
            status_code=404, detail={"Error": "Error occoured, try again"}
        )


@IntruderRouter.get("/detect/image/{image_uuid}", response_class=StreamingResponse)
async def image_get(image_uuid: UUID):
    """
    - **image_uuid** : Unique UUID to Search image in Database
    * Response will be the Image
        * Once the image is fetched it will be deleted from the database

    """
    _db = await MDBClient.get_db()
    _intruder = _db["intruder"]
    _intruder_images = _db["images"]
    try:
        data = await _intruder_images.find_one_and_delete({"uuid": str(image_uuid)})
        await _intruder.delete_one({"uuid": str(image_uuid)})
        image = base64.b64decode(data["image"])
        return StreamingResponse(io.BytesIO(image), media_type="image/jpeg")
    except KeyError as e:
        LOGGER.warning(f"Image not found in the database, Error : {e}")
        raise HTTPException(
            status_code=404,
            detail={"status": f"Image UUID {image_uuid} not found in the DB"},
        )


@IntruderRouter.get(
    "/images/uuids", response_class=ORJSONResponse, response_model=ImageUUID
)
async def uuids_get():
    """
    get all the available image UUID's in the Database according to the Priority

    """
    LOGGER.debug(f"Getting all the UUID's in the database")
    _db = await MDBClient.get_db()
    _intruder = _db["intruder"]
    n_docs = await _intruder.estimated_document_count()
    image_data = []
    if n_docs != 0:
        LOGGER.info(f"No of Pending Alerts found : {n_docs}")
        async for doc in _intruder.find({}, {"_id": False}).sort("_id").limit(n_docs):
            j_resp = jsonable_encoder(doc)
            image_data.append(j_resp)
        resp_dict = {"pending_alerts": n_docs, "image_data": image_data}
        return ORJSONResponse(content=resp_dict)
    else:
        LOGGER.warning(f"Nothing Found in the Database")
        raise HTTPException(
            status_code=404, detail={"status": "LMAO Nothing found dude"}
        )


@IntruderRouter.get(
    "/images/uuid/{image_uuid}",
    response_class=ORJSONResponse,
    response_model=IntruderInstantResponse,
)
async def get_using_uuid(image_uuid: UUID):
    """
    get all the available image UUID's in the Database according to the Priority

    """
    LOGGER.debug(f"Getting all the UUID's in the database")
    _db = await MDBClient.get_db()
    _intruder = _db["intruder"]
    data = await _intruder.find_one({"uuid": str(image_uuid)}, {"_id": False})
    if data is not None:
        j_resp = jsonable_encoder(data)
        LOGGER.debug(f"Data fetched using UUID {str(image_uuid)}: {j_resp}")
        return ORJSONResponse(content=j_resp)
    else:
        LOGGER.warning(f"Nothing Found in the Database")
        raise HTTPException(
            status_code=404, detail={"status": "LMAO Nothing found dude"}
        )
