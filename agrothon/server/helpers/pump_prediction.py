#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   pump_prediction.py
@Path    :   agrothon/server/helpers/
@Time    :   2021/05/5
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.2
@Contact :   ckvbalusu@gmail.com
@Desc    :   Pump Prediction Module
"""
import logging
from typing import Optional

import joblib
import numpy as np

pump_model = joblib.load("data/models/pump/pump.sav")

LOGGER = logging.getLogger(__name__)


async def predict_pump(
    moisture: float, temperature: float, humidity: float
) -> Optional[bool]:
    try:
        LOGGER.info(
            f"Predicting Pump using moisture: {moisture}, temperature: {temperature}, humidity: {humidity}"
        )
        prediction = pump_model.predict(np.array([[moisture, temperature, humidity]]))
        return bool(prediction[0])
    except Exception as e:
        LOGGER.error(f"Error Occured while predicting pump, Error : {e}")
        return None
