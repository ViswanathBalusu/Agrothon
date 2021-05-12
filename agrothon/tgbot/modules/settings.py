#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   settings.py
@Path    :   agrothon/tgbot/modules/
@Time    :   2021/05/9
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.1.5
@Contact :   ckvbalusu@gmail.com
@Desc    :   Settings Command handler
"""
import os
import time
from sys import executable

from agrothon import (
    FIELD_COMMAND,
    HELP_COMMAND,
    LANG,
    LOG_COMMAND,
    PING_COMMAND,
    RAIN_COMMAND,
    RESTART_COMMAND,
    SETTINGS_COMMAND,
    STATS_COMMAND,
    WEATHER_COMMAND,
)

from ..helpers.keyboards import settingskey


async def settings(client, message):
    await message.reply_text(text=LANG.SETTINGS, reply_markup=settingskey)


async def restart(client, message):
    restart_msg = await message.reply_text(text=LANG.RESTART)
    with open(".restartfile", "w") as r_file:
        r_file.truncate(0)
        r_file.write(f"{restart_msg.chat.id}\n{restart_msg.message_id}")
    os.execl(executable, executable, "-m", "agrothon")


async def start(client, message):
    await message.reply_text(text=LANG.START)


async def help_command(client, message):
    await message.reply_text(
        text=LANG.HELP_MESSAGE.format(
            WEATHER_COMMAND,
            RAIN_COMMAND,
            FIELD_COMMAND,
            SETTINGS_COMMAND,
            STATS_COMMAND,
            PING_COMMAND,
            LOG_COMMAND,
            RESTART_COMMAND,
            HELP_COMMAND,
        )
    )


async def ping_command(client, message):
    start_time = int(round(time.time() * 1000))
    ping_start = await message.reply_text(text=LANG.PING_START)
    end_time = int(round(time.time() * 1000))
    await ping_start.edit_text(text=LANG.PING_FINAL.format(f"{end_time-start_time} ms"))
