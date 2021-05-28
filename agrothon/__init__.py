#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Path    :   agrothon/
@Time    :   2021/05/24
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.3.1
@Contact :   ckvbalusu@gmail.com
@Desc    :   Initialization Module for Agrothon
"""

__VERSION__ = "1.3.1"

import logging
import os
import time

if os.path.exists("Agrothon.txt"):
    with open("Agrothon.txt", "r+") as f:
        f.truncate(0)
from .server.helpers.database import MongoClient

try:
    from AgroConfig import Config
except ModuleNotFoundError:
    from agrothon.BaseConfig import Config

from logging.handlers import RotatingFileHandler

from .tgbot.translations import setLang

# Logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("Agrothon.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


# Importing Variables from Config

SERVER_TIME = time.time()
TIME_Z = Config.TIME_ZONE
os.environ["TZ"] = Config.TIME_ZONE
time.tzset()
LANGUAGE = Config.LANGUAGE
OPEN_WEATHER_API = Config.OPEN_WEATHER_API
TELEGRAM_APP_ID = Config.TELEGRAM_APP_ID
TELEGRAM_API_HASH = Config.TELEGRAM_API_HASH
BOT_TOKEN = Config.BOT_TOKEN
LANG = setLang(LANGUAGE)
DEF_CITY = Config.DEF_CITY
API_KEY = Config.API_KEY
API_BASE_URL = Config.API_BASE_URL
if API_BASE_URL is not None:
    if not API_BASE_URL.endswith("/"):
        API_BASE_URL = API_BASE_URL + "/"
ALERT_CHANNEL_ID = Config.ALERT_CHANNEL_ID
DISTRICT = Config.DISTRICT
STATE = Config.STATE
DB_URL = Config.DB_URL
SENSOR_PRIORITY_INDEX = Config.SENSOR_PRIORITY_INDEX

# Commands
STATS_COMMAND = Config.STATS_COMMAND
FIELD_COMMAND = Config.FIELD_COMMAND
SETTINGS_COMMAND = Config.SETTINGS_COMMAND
WEATHER_COMMAND = Config.WEATHER_COMMAND
LOG_COMMAND = Config.LOG_COMMAND
HELP_COMMAND = Config.HELP_COMMAND
RAIN_COMMAND = Config.RAIN_COMMAND
RESTART_COMMAND = Config.RESTART_COMMAND
PING_COMMAND = Config.PING_COMMAND
AUTH_ID = Config.AUTH_ID

MDBClient = MongoClient(DB_URL)
