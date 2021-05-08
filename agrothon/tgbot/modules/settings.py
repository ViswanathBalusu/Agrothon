#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   settings.py
@Path    :   agrothon/tgbot/modules/
@Time    :   2021/05/8
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.1.0
@Contact :   ckvbalusu@gmail.com
@Desc    :   Settings Command handler
"""
import os
import time
from agrothon import LANG, SETTINGS_COMMAND, RESTART_COMMAND, HELP_COMMAND, PING_COMMAND, STATS_COMMAND, FIELD_COMMAND, WEATHER_COMMAND, LOG_COMMAND, RAIN_COMMAND
from sys import executable
from ..Client import AgroBot, filters
from ..helpers.keyboards import settingskey


@AgroBot.on_message(filters.command([SETTINGS_COMMAND]))
async def settings(client, message):
    await message.reply_text(text=LANG.SETTINGS, reply_markup=settingskey)


@AgroBot.on_message(filters.command([RESTART_COMMAND]))
async def restart(client, message):
    restart_msg = await message.reply_text(text=LANG.RESTART)
    with open(".restartfile", "w") as r_file:
        r_file.truncate(0)
        r_file.write(f"{restart_msg.chat.id}\n{restart_msg.message_id}")
    os.execl(executable, executable, "-m", "agrothon")


@AgroBot.on_message(filters.command(["start"]))
async def start(client, message):
    await message.reply_text(text=LANG.START)


@AgroBot.on_message(filters.command([HELP_COMMAND]))
async def help_command(client, message):
    await message.reply_text(text=LANG.HELP_MESSAGE.format(WEATHER_COMMAND, RAIN_COMMAND, FIELD_COMMAND, SETTINGS_COMMAND, STATS_COMMAND, PING_COMMAND, LOG_COMMAND, RESTART_COMMAND, HELP_COMMAND))


@AgroBot.on_message(filters.command([PING_COMMAND]))
async def ping_command(client, message):
    start_time = int(round(time.time() * 1000))
    ping_start = await message.reply_text(text=LANG.PING_START)
    end_time = int(round(time.time() * 1000))
    await ping_start.edit_text(text=LANG.PING_FINAL.format(f"{end_time-start_time} ms"))
