#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   rain_predict.py
@Path    :   agrothon/server/routers/
@Time    :   2021/05/5
@Author  :   Sreenivas Pakyala
@Version :   1.0.2
@Contact :   sreenivasseenu2904@gmail.com
@Desc    :   RainFall prediction Router
"""
import logging

from fastapi import APIRouter, HTTPException
from fastapi.responses import ORJSONResponse

from ..helpers.rainpredict import rainfall_predict
from ..helpers.response_models import RainPredictionOut, Region

LOGGER = logging.getLogger(__name__)


RainPredictRouter = APIRouter(
    prefix="/rainfall",
    tags=["Rainfall Prediction"],
    responses={404: {"error": "Not found"}},
)


@RainPredictRouter.post(
    "/predict", response_class=ORJSONResponse, response_model=RainPredictionOut
)
async def predict_rainfall(region: Region):
    """
    **Predict Rainfall of the Region based on Previous year's data**
    - **state** : State name
        - ex : Andhra Pradesh
    - **district** : District name
        - ex: East Godavari
    *Returns*
    - Rainfall Predictions between April and December
        - Because in india rainfall mostly happens between these months
    """
    l_state = region.state.lower()
    l_district = region.district.lower()
    u_state = l_state.upper()
    u_district = l_district.upper()
    predictions = rainfall_predict(u_state, u_district)
    response_dict = {
        "state": l_state.title(),
        "district": l_district.title(),
        "units": "mm",
    }
    if predictions is not None:
        response_dict["predictions"] = predictions
        return ORJSONResponse(content=response_dict)
    else:
        raise HTTPException(
            status_code=404, detail={"error": "Check state and district names"}
        )
