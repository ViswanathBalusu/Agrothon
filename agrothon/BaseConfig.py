#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   BaseConfig.py
@Path    :   agrothon/
@Time    :   2021/05/24
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.2.7
@Contact :   ckvbalusu@gmail.com
@Desc    :   Base Configuration for Agrothon
"""
import os

from dotenv import load_dotenv

load_dotenv("agrothon.env")


class Config(object):

    # Telegram
    TELEGRAM_APP_ID = int(os.environ.get("TELEGRAM_APP_ID", -1))
    TELEGRAM_API_HASH = os.environ.get("TELEGRAM_API_HASH", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    API_BASE_URL = os.environ.get("API_BASE_URL", None)
    ALERT_CHANNEL_ID = int(os.environ.get("ALERT_CHANNEL_ID", -1))
    STATE = os.environ.get("STATE", None)
    DISTRICT = os.environ.get("DISTRICT", None)
    DEF_CITY = os.environ.get("DEF_CITY", None)
    LANGUAGE = os.environ.get("DEF_LANG", "english")

    # Bot Commands
    STATS_COMMAND = os.environ.get("STATS_COMMAND", "stats")
    FIELD_COMMAND = os.environ.get("FIELD_COMMAND", "field")
    SETTINGS_COMMAND = os.environ.get("SETTINGS_COMMAND", "settings")
    WEATHER_COMMAND = os.environ.get("WEATHER_COMMAND", "weather")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "log")
    HELP_COMMAND = os.environ.get("HELP_COMMAND", "help")
    RAIN_COMMAND = os.environ.get("RAIN_COMMAND", "rainfall")
    RESTART_COMMAND = os.environ.get("RESTART_COMMAND", "restart")
    PING_COMMAND = os.environ.get("PING_COMMAND", "ping")

    # API Server
    OPEN_WEATHER_API = os.environ.get("OPEN_WEATHER_API", None)
    API_KEY = os.environ.get("API_KEY", None)
    DB_URL = os.environ.get("DB_URL", None)
    TIME_ZONE = os.environ.get("TIME_ZONE", "Asia/Kolkata")
    try:
        SENSOR_PRIORITY_INDEX = int(os.environ.get("SENSOR_PRIORITY", 1))
    except BaseException:
        SENSOR_PRIORITY_INDEX = 1
