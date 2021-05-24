#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   openweather.py
@Path    :   agrothon/server/routers/
@Time    :   2021/05/3
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.2.6
@Contact :   ckvbalusu@gmail.com
@Desc    :   OpenWeather data router
"""

import logging

from fastapi import APIRouter, HTTPException
from fastapi.responses import ORJSONResponse

from ..helpers.openwapi import open_weather_helper_city
from ..helpers.response_models import Weather

LOGGER = logging.getLogger(__name__)

OpenWeatherRouter = APIRouter(
    prefix="/weather",
    tags=["Weather"],
    responses={404: {"error": "Not found"}},
)


@OpenWeatherRouter.get("/{city}", response_class=ORJSONResponse, response_model=Weather)
async def weather_get(city: str):
    """
    Open Weather API Wrapper
    - **city** : City from which the weather data should be fetched (Optional)
    * returns
        * city
        * temperature
        * pressure
        * humidity
        * weather description
    """
    LOGGER.info(f"Getting Weather for {city}")
    status, resp = await open_weather_helper_city(city)
    if status:
        main = resp["main"]
        return ORJSONResponse(
            content={
                "city": resp["name"],
                "temperature": main["temp"],
                "pressure": main["pressure"],
                "humidity": main["humidity"],
                "weather": resp["weather"][0]["description"],
            }
        )
    else:
        raise HTTPException(status_code=404, detail={"error": "API Request Error"})
