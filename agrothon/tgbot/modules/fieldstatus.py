#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   fieldstatus.py
@Path    :   agrothon/tgbot/modules/
@Time    :   2021/05/8
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.1.0
@Contact :   ckvbalusu@gmail.com
@Desc    :   Field Status Command handler
"""
from agrothon import FIELD_COMMAND, LANG

from ..Client import AgroBot, filters
from ..helpers.keyboards import fieldkey


@AgroBot.on_message(filters.command([FIELD_COMMAND]))
async def field(client, message):
    await message.reply_text(text=LANG.MAIN_MENU, reply_markup=fieldkey)
