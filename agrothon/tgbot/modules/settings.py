#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   settings.py
@Path    :   agrothon/tgbot/modules/
@Time    :   2021/05/3
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.0
@Contact :   ckvbalusu@gmail.com
@Desc    :   Settings Command handler
"""

from agrothon import LANG

from ..Client import AgroBot, filters
from ..helpers.keyboards import settingskey


@AgroBot.on_message(filters.command(["settings"]))
async def settings(client, message):
    await message.reply_text(text=LANG.SETTINGS, reply_markup=settingskey)
