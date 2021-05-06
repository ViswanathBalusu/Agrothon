#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   response_models.py
@Path    :   agrothon/server/helpers/
@Time    :   2021/05/5
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.2
@Contact :   ckvbalusu@gmail.com
@Desc    :   Response and Accept Models
"""
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


class SuccessResponseSensor(BaseModel):
    Success: bool
    pump_status_updated: bool


class SuccessResponse(BaseModel):
    Success: bool


class PumpGetResponse(BaseModel):
    status: bool
    by: str
    time: str
    last_read: Optional[str] = None


class PumpPostIN(BaseModel):
    status: bool
    by: str

    class Config:
        schema_extra = {
            "example": {
                "status": True,
                "by": "A Person",
            }
        }


class ImageSuccessResponse(BaseModel):
    Detected_Intruders: bool
    uuid: UUID


class Weather(BaseModel):
    city: str
    temperature: int
    pressure: int
    humidity: int
    weather: str


class Sensor(BaseModel):
    moisture: float
    humidity: float
    temperature: float
    updated_at: str
    pump_prediction: bool
    last_read: Optional[str] = None


class SensorData(BaseModel):
    moisture: float
    humidity: float
    temperature: float

    class Config:
        schema_extra = {
            "example": {
                "moisture": 19.25,
                "humidity": 20.95,
                "temperature": 35,
            }
        }


class SensorBase(BaseModel):
    moisture: int
    humidity: int
    temperature: int
    updated_at: str

    class Config:
        schema_extra = {
            "example": {
                "moisture": 19.25,
                "humidity": 20.95,
                "temperature": 35,
                "updated_at": "15:35:53 05/02/21",
            }
        }


class SensorAll(BaseModel):
    no_of_entries: int
    sensor_data: List[SensorBase]


class IntruderDetections(BaseModel):
    type: str
    confidences: List[float]
    count: int


class IntruderInstantResponse(BaseModel):
    uuid: UUID
    detections: List[IntruderDetections]
    no_of_detections: int
    humans: int
    only_humans: bool
    at: str


class ImageUUID(BaseModel):
    pending_alerts: int
    image_data: List[IntruderInstantResponse]


class Region(BaseModel):
    state: str
    district: str

    class Config:
        schema_extra = {
            "example": {
                "state": "Andhra Pradesh",
                "district": "East Godavari",
            }
        }


class MonthWisePrediction(BaseModel):
    april: float
    may: float
    june: float
    july: float
    august: float
    september: float
    october: float
    november: float
    december: float


class RainPredictionOut(BaseModel):
    state: str
    district: str
    units: str
    predictions: MonthWisePrediction
