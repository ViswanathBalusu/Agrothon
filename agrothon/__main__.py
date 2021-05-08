#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   __main__.py
@Path    :   agrothon/
@Time    :   2021/05/8
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.1.0
@Contact :   ckvbalusu@gmail.com
@Desc    :   Main Module for Agrothon
"""
import logging
from threading import Thread
from agrothon import LOGGER
from .AlertBot import alerts_handler, restart_check, language_change_check
from .tgbot.Client import AgroBot

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.INFO)
# LOGGER = logging.getLogger(__name__)


if __name__ == "__main__":
    restart_check()
    language_change_check()
    LOGGER.info("Starting Bot")
    Thread(target=alerts_handler, daemon=True).start()
    AgroBot().run()
