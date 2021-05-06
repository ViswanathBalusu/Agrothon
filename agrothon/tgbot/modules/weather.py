#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   weather.py
@Path    :   agrothon/tgbot/modules/
@Time    :   2021/05/3
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.0
@Contact :   ckvbalusu@gmail.com
@Desc    :   Weather Command handler
"""

from agrothon import DEF_CITY, LANG

from ..Client import AgroBot, filters
from ..helpers.apiserverhelper import open_weather


@AgroBot.on_message(filters.command(["weather"]))
async def weather(client, message):
    init = await message.reply_text("Fetching Details Please Wait")
    response = await open_weather(DEF_CITY)
    if response is not None:
        msg = LANG.WEATHER.format(
            response["city"],
            response["temperature"],
            response["pressure"],
            response["humidity"],
            response["weather"],
        )
        await init.edit_text(msg)
    else:
        await init.edit_text(LANG.WEATHER_ERR.format())
