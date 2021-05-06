#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   pump.py
@Path    :   agrothon/server/routers/
@Time    :   2021/05/3
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.0
@Contact :   ckvbalusu@gmail.com
@Desc    :   Pump on or off Router
"""
import logging
from datetime import datetime

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse

from agrothon import MDBClient

from ..helpers.response_models import PumpGetResponse, PumpPostIN, SuccessResponse

LOGGER = logging.getLogger(__name__)


PumpRouter = APIRouter(
    prefix="/pump",
    tags=["Pump"],
    responses={404: {"error": "Not found"}},
)


@PumpRouter.get("/", response_class=ORJSONResponse, response_model=PumpGetResponse)
async def pump_get():
    """
    **Pump Status**
    - Will return the present status  of the pump in the field
    """
    LOGGER.info(f"Getting Pump status")
    _db = await MDBClient.get_db()
    _pump = _db["pump"]
    now = datetime.now()
    time_date = now.strftime("%X %x")
    try:
        data = await _pump.find_one({"_id": "pump"}, {"_id": False})
        if data is not None:
            await _pump.update_one(
                {"_id": "pump"}, {"$set": {"last_read": time_date}}, upsert=True
            )
            j_resp = jsonable_encoder(data)
            LOGGER.debug(f"Pump status : {str(j_resp)}")
            return ORJSONResponse(content=j_resp)
        else:
            raise HTTPException(
                status_code=404, detail={"error": "Nothing found to Query"}
            )
    except AttributeError as e:
        LOGGER.error(f"Error Occurred while getting Pump Status : {e}")
        raise HTTPException(
            status_code=404, detail={"error": "Something wrong with the database"}
        )


@PumpRouter.post("/", response_class=ORJSONResponse, response_model=SuccessResponse)
async def pump_post(status: PumpPostIN):
    """
    **Update Pump Status in the field**
    """
    LOGGER.info(f"Updating Pump Status")
    _db = await MDBClient.get_db()
    _pump = _db["pump"]
    now = datetime.now()
    time_date = now.strftime("%X %x")
    try:
        await _pump.update_one(
            {"_id": "pump"},
            {
                "$set": {
                    "status": status.status,
                    "time": time_date,
                    "by": status.by,
                    "last_read": time_date,
                }
            },
            upsert=True,
        )
        j_resp = jsonable_encoder({"Success": True})
        return ORJSONResponse(content=j_resp)
    except Exception as e:
        LOGGER.error(f"Error Occurred while Updating Pump Status : {e}")
        raise HTTPException(status_code=404, detail={"error": "Cant Post"})
