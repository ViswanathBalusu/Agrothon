#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   fieldstatus.py
@Path    :   agrothon/tgbot/modules/
@Time    :   2021/05/9
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.1.5
@Contact :   ckvbalusu@gmail.com
@Desc    :   Field Status Command handler
"""
from agrothon import LANG

from ..helpers.keyboards import fieldkey


async def field(client, message):
    await message.reply_text(text=LANG.MAIN_MENU, reply_markup=fieldkey)
