#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   apiserverhelper.py
@Path    :   agrothon/tgbot/helpers/
@Time    :   2021/05/6
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.3
@Contact :   ckvbalusu@gmail.com
@Desc    :   API Server request helper
"""
from typing import Optional

import aiohttp
import requests

from agrothon import API_BASE_URL, API_KEY


async def aiohttp_helper(
    url: str, headers: dict, data: Optional[dict] = None, method: Optional[str] = "get"
):
    async with aiohttp.ClientSession() as session:
        if method == "get":
            async with session.get(url=url, headers=headers) as response:
                if response.status == 200:
                    try:
                        data = await response.json()
                        return True, data
                    except AttributeError:
                        return False, None
                else:
                    return False, None
        elif method == "post":
            async with session.post(url=url, json=data, headers=headers) as response:
                if response.status == 200:
                    try:
                        data = await response.json()
                        return True, data
                    except AttributeError:
                        return False, None
                else:
                    return False, None
        else:
            return False, None


async def pump_get():
    url = f"{API_BASE_URL}pump/?api_key={API_KEY}"
    headers = {"accept": "application/json"}
    status, response = await aiohttp_helper(url=url, headers=headers)
    if status:
        return response
    else:
        return None


async def pump_post(status: bool, by: Optional[str] = "User"):
    url = f"{API_BASE_URL}pump/?api_key={API_KEY}"
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    data = {"status": status, "by": by}
    status, response = await aiohttp_helper(
        url=url, headers=headers, data=data, method="post"
    )
    if status:
        return response
    else:
        return None


async def sensor_get_latest():
    url = f"{API_BASE_URL}field/sensor?api_key={API_KEY}"
    headers = {"accept": "application/json"}
    status, response = await aiohttp_helper(url=url, headers=headers)
    if status:
        return response
    else:
        return None


async def sensor_get_all():
    url = f"{API_BASE_URL}field/sensor/all/?api_key={API_KEY}"
    headers = {"accept": "application/json"}
    status, response = await aiohttp_helper(url=url, headers=headers)
    if status:
        return response
    else:
        return None


async def open_weather(city: str):
    url = f"{API_BASE_URL}weather/{city}?api_key={API_KEY}"
    headers = {"accept": "application/json"}
    status, response = await aiohttp_helper(url=url, headers=headers)
    if status:
        return response
    else:
        return None


def get_image_uuids():
    url = f"{API_BASE_URL}intruder/images/uuids?api_key={API_KEY}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        resp = response.json()
        return resp
    else:
        return None


def get_image_url(uuid: str):
    url = f"{API_BASE_URL}intruder/detect/image/{uuid}?api_key={API_KEY}"
    return url


async def get_rainfall_prediction(state: str, district: str):
    url = f"{API_BASE_URL}rainfall/predict?api_key={API_KEY}"
    headers = {"accept": "application/json"}
    data = {"state": state, "district": district}
    status, response = await aiohttp_helper(
        url=url, headers=headers, data=data, method="post"
    )
    if status:
        return response
    else:
        return None


async def get_instant_image_url(uuid: str):
    url = f"{API_BASE_URL}intruder/detect/instant/{uuid}?api_key={API_KEY}"
    return url


async def upload_file_to_api(path):
    url = f"{API_BASE_URL}intruder/detect/instant?api_key={API_KEY}"
    with open(path, "rb") as file:
        files = {"image": file}
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, data=files) as response:
                if response.status == 200:
                    try:
                        data = await response.json()
                        image_url = await get_instant_image_url(data["uuid"])
                        del data["uuid"]
                        data["image_url"] = image_url
                        return True, data
                    except AttributeError:
                        return False, None
                else:
                    return False, None
