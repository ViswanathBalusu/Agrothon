#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   __main__.py
@Path    :   agrothon/
@Time    :   2021/05/4
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.1
@Contact :   ckvbalusu@gmail.com
@Desc    :   Main Module for Agrothon
"""
import logging
from threading import Thread

from .AlertBot import alerts_handler
from .tgbot.Client import AgroBot

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.INFO)
LOGGER = logging.getLogger(__name__)


if __name__ == "__main__":
    Thread(target=alerts_handler, daemon=True).start()
    AgroBot().run()
