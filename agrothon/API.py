#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   API.py
@Path    :   agrothon/
@Time    :   2021/05/5
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.2
@Contact :   ckvbalusu@gmail.com
@Desc    :   Main module which starts API Server
"""
import logging

from fastapi import FastAPI, Security

from agrothon import __VERSION__, MDBClient

from .server.helpers.api_key_helper import verify_api_key
from .server.routers import intruder, openweather, pump, rain_predict, sensors

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("multpart").setLevel(logging.WARNING)


Agrothon = FastAPI(
    title="Agrothon",
    version=__VERSION__,
    docs_url="/docs",
    redoc_url=None,
    openapi_url="/Agrothon.json",
    dependencies=[Security(verify_api_key)],
)
Agrothon.add_event_handler("startup", MDBClient.connect_db)
Agrothon.add_event_handler("shutdown", MDBClient.close_mongo_connection)
Agrothon.include_router(intruder.IntruderRouter)
Agrothon.include_router(openweather.OpenWeatherRouter)
Agrothon.include_router(pump.PumpRouter)
Agrothon.include_router(sensors.SensorRouter)
Agrothon.include_router(rain_predict.RainPredictRouter)
