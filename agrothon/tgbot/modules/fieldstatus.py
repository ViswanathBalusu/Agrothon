#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   fieldstatus.py
@Path    :   agrothon/tgbot/modules/
@Time    :   2021/05/3
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.0
@Contact :   ckvbalusu@gmail.com
@Desc    :   Field Status Command handler
"""
from agrothon import LANG

from ..Client import AgroBot, filters
from ..helpers.keyboards import fieldkey


@AgroBot.on_message(filters.command(["field"]))
async def field(client, message):
    await message.reply_text(text=LANG.MAIN_MENU, reply_markup=fieldkey)
