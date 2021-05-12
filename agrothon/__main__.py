#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   __main__.py
@Path    :   agrothon/
@Time    :   2021/05/8
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.1.4
@Contact :   ckvbalusu@gmail.com
@Desc    :   Main Module for Agrothon
"""
import logging
from threading import Thread

from pyrogram import Client, filters
from pyrogram.handlers import CallbackQueryHandler, MessageHandler

from agrothon import (
    BOT_TOKEN,
    FIELD_COMMAND,
    HELP_COMMAND,
    LOG_COMMAND,
    LOGGER,
    PING_COMMAND,
    RAIN_COMMAND,
    RESTART_COMMAND,
    SETTINGS_COMMAND,
    STATS_COMMAND,
    TELEGRAM_API_HASH,
    TELEGRAM_APP_ID,
    WEATHER_COMMAND,
)

from .AlertBot import alerts_handler, language_change_check, restart_check
from .tgbot.modules.callbacks import (
    backcbq,
    callback_sensors,
    lang_change,
    languages,
    pumpque,
    restart_callback,
)
from .tgbot.modules.fieldstatus import field
from .tgbot.modules.photo_handler import photo_detect
from .tgbot.modules.rainfall import rainfall_predict
from .tgbot.modules.settings import help_command, ping_command, restart, settings, start
from .tgbot.modules.utils import send_log, stats
from .tgbot.modules.weather import weather

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.INFO)

AgroBot = Client(
    "Agrothon",
    bot_token=BOT_TOKEN,
    api_id=TELEGRAM_APP_ID,
    api_hash=TELEGRAM_API_HASH,
    workers=20,
    device_model="Agrothon",
)

# Callback Query handlers
cb_sensors = CallbackQueryHandler(
    callback_sensors,
    filters=filters.regex(pattern="^moisture|humidity|temperature|complete$"),
)
AgroBot.add_handler(cb_sensors)

back_cbq = CallbackQueryHandler(backcbq, filters=filters.regex(pattern="^back|exit$"))
AgroBot.add_handler(back_cbq)

pump_que = CallbackQueryHandler(
    pumpque, filters=filters.regex(pattern="^pumpstat|pumpon|pumpoff|refresh|bot$")
)
AgroBot.add_handler(pump_que)

languages_ = CallbackQueryHandler(
    languages, filters=filters.regex(pattern="^eng|tel|tam|hin$")
)
AgroBot.add_handler(languages_)

lang_hand = CallbackQueryHandler(lang_change, filters=filters.regex(pattern="^lang$"))
AgroBot.add_handler(lang_hand)

rsrt_hand = CallbackQueryHandler(
    restart_callback, filters=filters.regex(pattern="^restart$")
)
AgroBot.add_handler(rsrt_hand)

# Command Handlers

field_hand = MessageHandler(field, filters=filters.command([FIELD_COMMAND]))
AgroBot.add_handler(field_hand)

phot_detect = MessageHandler(photo_detect, filters=filters.photo & filters.private)
AgroBot.add_handler(phot_detect)

rain_hand = MessageHandler(rainfall_predict, filters=filters.command([RAIN_COMMAND]))
AgroBot.add_handler(rain_hand)

set_hand = MessageHandler(settings, filters=filters.command([SETTINGS_COMMAND]))
AgroBot.add_handler(set_hand)

rest_hand = MessageHandler(restart, filters=filters.command([RESTART_COMMAND]))
AgroBot.add_handler(rest_hand)

start_hand = MessageHandler(start, filters=filters.command(["start"]))
AgroBot.add_handler(start_hand)

help_hand = MessageHandler(help_command, filters=filters.command([HELP_COMMAND]))
AgroBot.add_handler(help_hand)

ping_hand = MessageHandler(ping_command, filters=filters.command([PING_COMMAND]))
AgroBot.add_handler(ping_hand)

stats_hand = MessageHandler(stats, filters=filters.command([STATS_COMMAND]))
AgroBot.add_handler(stats_hand)

log_hand = MessageHandler(send_log, filters=filters.command([LOG_COMMAND]))
AgroBot.add_handler(log_hand)

weather_hand = MessageHandler(weather, filters=filters.command([WEATHER_COMMAND]))
AgroBot.add_handler(weather_hand)


def main():
    restart_check()
    language_change_check()
    LOGGER.info("Starting Bot")
    Thread(target=alerts_handler, daemon=True).start()
    AgroBot.run()


if __name__ == "__main__":
    main()
