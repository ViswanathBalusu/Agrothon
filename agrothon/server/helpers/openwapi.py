#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   openwapi.py
@Path    :   agrothon/server/helpers/
@Time    :   2021/05/5
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.2
@Contact :   ckvbalusu@gmail.com
@Desc    :   Open Weather API Request Module
"""
from typing import Dict, Optional, Tuple

import aiohttp

from agrothon import LOGGER, OPEN_WEATHER_API


async def open_weather_helper_city(city: str) -> Tuple[bool, Optional[Dict]]:
    async with aiohttp.ClientSession() as session:
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER_API}&units=metric"
        LOGGER.debug("Making URL Request: " + api_url)
        async with session.get(api_url) as response:
            if response.status == 200:
                LOGGER.info(
                    f"Got Open Weather API response : {str(await response.json())}"
                )
                resp = await response.json()
                return True, resp
            else:
                LOGGER.error(f"Error in making API Request : {str(response.json())}")
                return False, None
