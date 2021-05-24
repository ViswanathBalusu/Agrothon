#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   sensors.py
@Path    :   agrothon/server/routers/
@Time    :   2021/05/5
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.2.7
@Contact :   ckvbalusu@gmail.com
@Desc    :   Sensors data post or get Routers
"""
import logging
from datetime import datetime

import orjson
from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse

from agrothon import SENSOR_PRIORITY_INDEX, MDBClient

from ..helpers.pump_prediction import predict_pump
from ..helpers.response_models import (
    Sensor,
    SensorAll,
    SensorData,
    SuccessResponseSensor,
)

LOGGER = logging.getLogger(__name__)


SensorRouter = APIRouter(
    prefix="/field",
    tags=["Field Data"],
    responses={404: {"error": "Not found"}},
)


@SensorRouter.get("/sensor", response_class=ORJSONResponse, response_model=Sensor)
async def sensor_get():
    """
    Get the Last Update of the sensor data
    """
    LOGGER.info(f"Getting Sensor data from the database")
    _db = await MDBClient.get_db()
    _sensor = _db["sensor"]
    now = datetime.now()
    time_date = now.strftime("%X %x")
    try:
        n_docs = await _sensor.estimated_document_count()
        latest_doc_id = int(n_docs) - 1
        data = await _sensor.find_one({"_id": latest_doc_id}, {"_id": False})
        await _sensor.update_one(
            {"_id": latest_doc_id}, {"$set": {"last_read": time_date}}
        )
        j_resp = jsonable_encoder(data)
        LOGGER.debug(f"Fetched sensor data : {j_resp}")
        return ORJSONResponse(content=j_resp)
    except Exception as e:
        LOGGER.error(f"Error Occurred While getting data from database, Error: {e}")
        raise HTTPException(status_code=404, detail={"error": "Nothing Found"})


@SensorRouter.get(
    "/sensor/all", response_class=ORJSONResponse, response_model=SensorAll
)
async def sensor_get_all():
    """
    **Get all the Sensor data from the database**
    """
    LOGGER.info("Getting all the available sensor data from database")
    _db = await MDBClient.get_db()
    _sensor = _db["sensor"]
    n_docs = await _sensor.estimated_document_count()
    sensor_data = []
    if n_docs != 0:
        async for doc in _sensor.find({}, {"_id": False, "last_read": False}).sort(
            "_id"
        ).limit(n_docs):
            sensor_data.append(jsonable_encoder(doc))
        LOGGER.info(f"Fetched {n_docs} entries of sensor data")
        return ORJSONResponse(
            content={"no_of_entries": n_docs, "sensor_data": sensor_data}
        )
    else:
        raise HTTPException(status_code=404, detail={"error": "Nothing Found"})


@SensorRouter.post(
    "/sensor", response_class=ORJSONResponse, response_model=SuccessResponseSensor
)
async def sensor_post(data: SensorData):
    """
    **post sensor data from the field to DB**
    - Accepts Temperature, Humidity, Temperature as JSON
    """
    LOGGER.info(f"Parsing Sensor data that was posted")
    _db = await MDBClient.get_db()
    _sensor = _db["sensor"]
    _pump = _db["pump"]
    now = datetime.now()
    time_date: str = now.strftime("%X %x")
    pump_data = await _pump.find_one({"_id": "pump"}, {"_id": False})
    pump_set = False
    pump_stat = await predict_pump(
        data.moisture[SENSOR_PRIORITY_INDEX - 1], data.temperature, data.humidity
    )
    try:
        try:
            if pump_data["by"] == "AI Bot":
                if pump_data["status"]:
                    if pump_stat:
                        pump_set = False
                    else:
                        pump_set = True
                else:
                    if pump_stat:
                        pump_set = True
                    else:
                        pump_set = False
            else:
                pump_set = False
        except TypeError:
            pump_set = True
        n_docs = await _sensor.estimated_document_count()
        new_doc_id = int(n_docs)
        data_dict = {
            "no_of_sensors": data.no_of_sensors,
            "moisture": data.moisture,
            "humidity": data.humidity,
            "temperature": data.temperature,
            "pump_prediction": pump_stat,
            "sensor_priority": SENSOR_PRIORITY_INDEX,
            "updated_at": time_date,
            "last_read": time_date,
        }
        await _sensor.update_one(
            {"_id": new_doc_id},
            {"$set": data_dict},
            upsert=True,
        )
        if pump_set:
            pump_dict = {
                "status": pump_stat,
                "time": time_date,
                "by": "AI Bot",
                "last_read": time_date,
            }
            await _pump.update_one(
                {"_id": "pump"},
                {"$set": pump_dict},
                upsert=True,
            )
            LOGGER.debug(
                f"Pump Status has been updated : {str(orjson.dumps(pump_dict))}"
            )
        j_resp = {"Success": True, "pump_status_updated": pump_set}
        LOGGER.debug(f"Sensor Post response : {str(j_resp)}")
        return ORJSONResponse(content=j_resp)
    except Exception as e:
        LOGGER.error(f"Error Occurred while Updating :{e}")
        j_resp = jsonable_encoder({"Success": False})
        return ORJSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=j_resp
        )
