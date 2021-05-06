#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   Client.py
@Path    :   agrothon/tgbot/
@Time    :   2021/05/3
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.0
@Contact :   ckvbalusu@gmail.com
@Desc    :   Pyrogram Client module
"""
import datetime

from pyrogram import *

from agrothon import BOT_TOKEN, LOGGER, TELEGRAM_API_HASH, TELEGRAM_APP_ID


class AgroBot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()

        super().__init__(
            name,
            api_id=TELEGRAM_APP_ID,
            api_hash=TELEGRAM_API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "agrothon.tgbot.modules"},
            workers=20,
            device_model="Agrothon",
        )

    async def start(self):
        await super().start()
        LOGGER.info(f"Hey Bot Started {datetime.datetime.now()}")

    async def stop(self, *args):
        LOGGER.info(f"Stopping Bot {datetime.datetime.now()}")
        await super().stop()
