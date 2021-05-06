#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   BaseConfig.py
@Path    :   agrothon/
@Time    :   2021/05/4
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.1
@Contact :   ckvbalusu@gmail.com
@Desc    :   Base Configuration for Agrothon
"""
import os

from dotenv import load_dotenv

load_dotenv("agrothon.env")


class Config(object):

    # Telegram
    TELEGRAM_APP_ID = os.environ.get("TELEGRAM_APP_ID", "")
    TELEGRAM_API_HASH = os.environ.get("TELEGRAM_API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    PORT = os.environ.get("PORT", "10808")
    API_BASE_URL = os.environ.get("API_BASE_URL", f"http://localhost:{PORT}/")
    ALERT_CHANNEL_ID = int(os.environ.get("ALERT_CHANNEL_ID", -1))
    STATE = os.environ.get("STATE", "Andhra Pradesh")
    DISTRICT = os.environ.get("DISTRICT", "East Godavari")

    # API Server
    OPEN_WEATHER_API = os.environ.get("OPEN_WEATHER_API", "")
    DEF_CITY = os.environ.get("DEF_CITY", "")
    LANGUAGE = os.environ.get("LANGUAGE", "english")
    API_KEY = os.environ.get("API_KEY", "Chandu")
    DB_URL = os.environ.get("DB_URL", "mongodb://localhost:27017/")
