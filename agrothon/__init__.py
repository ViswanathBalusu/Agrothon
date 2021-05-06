#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Path    :   agrothon/
@Time    :   2021/05/6
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.3
@Contact :   ckvbalusu@gmail.com
@Desc    :   Initialization Module for Agrothon
"""

__VERSION__ = "1.0.3"

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
LANGUAGE = Config.LANGUAGE
OPEN_WEATHER_API = Config.OPEN_WEATHER_API
TELEGRAM_APP_ID = Config.TELEGRAM_APP_ID
TELEGRAM_API_HASH = Config.TELEGRAM_API_HASH
BOT_TOKEN = Config.BOT_TOKEN
LANG = setLang(LANGUAGE)
DEF_CITY = Config.DEF_CITY
API_KEY = Config.API_KEY
API_BASE_URL = Config.API_BASE_URL
if not API_BASE_URL.endswith("/"):
    API_BASE_URL = API_BASE_URL + "/"
ALERT_CHANNEL_ID = Config.ALERT_CHANNEL_ID
DISTRICT = Config.DISTRICT
STATE = Config.STATE
DB_URL = Config.DB_URL

MDBClient = MongoClient(DB_URL)
