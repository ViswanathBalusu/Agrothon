#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   rainfall.py
@Path    :   agrothon/tgbot/modules/
@Time    :   2021/05/8
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.1.0
@Contact :   ckvbalusu@gmail.com
@Desc    :   Rainfall prediction module for Telegram bot
"""
from prettytable import PrettyTable

from agrothon import DISTRICT, LANG, RAIN_COMMAND, STATE

from ..Client import AgroBot, filters
from ..helpers.apiserverhelper import get_rainfall_prediction

MONTHS = [
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]


@AgroBot.on_message(filters.command([RAIN_COMMAND]))
async def rainfall_predict(client, message):
    data = await get_rainfall_prediction(STATE, DISTRICT)
    if data is not None:
        units = data["units"]
        predictions = data["predictions"]
        pt = PrettyTable([LANG.MONTH, LANG.RAINFALL.format(units)])
        pt.align[LANG.MONTH] = "l"
        pt.align[LANG.RAINFALL.format(units)] = "c"
        pt.padding_width = 0
        i = 0
        for month in MONTHS:
            pt.add_row([LANG.MONTHS[i], predictions[month]])
            i += 1
        await message.reply_text(
            text=LANG.RAIN_PREDICT.format(STATE, DISTRICT, pt), parse_mode="HTML"
        )
    else:
        await message.reply_text(text=LANG.RAIN_PREDICT_ERR)
