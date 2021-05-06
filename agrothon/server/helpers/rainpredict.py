#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   rainpredict.py
@Path    :   agrothon/server/helpers/
@Time    :   2021/05/5
@Author  :   Sreenivas Pakyala
@Version :   1.0.3
@Contact :   sreenivasseenu2904@gmail.com
@Desc    :   Rain Prediction Deep learning Module
"""

from keras.models import model_from_json
import tensorflow as tf
import logging
import os
from typing import Optional, Dict
import numpy as np
import pandas as pd

tf.get_logger().setLevel("ERROR")
tf.autograph.set_verbosity(3)
LOGGER = logging.getLogger(__name__)


with open("data/models/rainfall/rainfall_model.json") as json_file:
    loaded_model = model_from_json(json_file.read())
csv_data = pd.read_csv("data/models/rainfall/india_rainfall.csv")
loaded_model.load_weights("data/models/rainfall/rainfall_model.h5")
_MONTHS = [
    "DISTRICT",
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC",
]
MONTHS = [
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC",
]
MONTHS_ = [
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]


def rainfall_predict(state: str, district: str) -> Optional[Dict]:
    try:
        LOGGER.info(f"Getting predictions for {district} in {state}")
        filter_state = csv_data[_MONTHS].loc[csv_data["STATE/UT"] == state]
        filter_district = np.asarray(
            filter_state[MONTHS].loc[filter_state["DISTRICT"] == district]
        )
        x_year = None
        for i in range(filter_district.shape[1] - 3):
            if x_year is None:
                x_year = filter_district[:, i : i + 3]
            else:
                x_year = np.concatenate((x_year, filter_district[:, i : i + 3]), axis=0)
        y_year_pred = loaded_model.predict(np.expand_dims(x_year, axis=2))
        predictions_dict = {}
        if y_year_pred is not None:
            for i in range(len(y_year_pred)):
                predictions_dict[MONTHS_[i]] = round(float(y_year_pred[i]), 2)
            LOGGER.debug(f"Predicted Rainfall Successfully : {str(predictions_dict)}")
            return predictions_dict
        else:
            LOGGER.error(f"Prediction of rainfall returned None")
            return None
    except Exception as e:
        LOGGER.error(f"Error in predicting Rainfall : {e}")
        return None
