#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   keyboards.py
@Path    :   agrothon/tgbot/helpers/
@Time    :   2021/05/3
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.0
@Contact :   ckvbalusu@gmail.com
@Desc    :   Keyboards used in the telegram bot
"""

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from agrothon import LANG

fieldkey = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("💧 " + LANG.MOISTURE, callback_data="moisture"),
            InlineKeyboardButton("⛅ " + LANG.HUMIDITY, callback_data="humidity"),
        ],
        [
            InlineKeyboardButton("🌡️ " + LANG.TEMPERATURE, callback_data="temperature"),
            InlineKeyboardButton("✅ " + LANG.COMPLETE_INFO, callback_data="complete"),
        ],
        [InlineKeyboardButton("🚰 " + LANG.PUMP_STATUS, callback_data="pumpstat")],
        [InlineKeyboardButton("🛑 " + LANG.QUIT, callback_data="exit")],
    ]
)


sepkeyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("🚰 " + LANG.PUMP_STATUS, callback_data="pumpstat")],
        [InlineKeyboardButton("⬅️ " + LANG.BACK, callback_data="back")],
    ]
)

pumpoffkey = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🛑 " + LANG.PUMP_OFF, callback_data="pumpoff"),
        ],
        [InlineKeyboardButton("⬅️ " + LANG.BACK, callback_data="pumpstat")],
    ]
)

pumponkey = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("✅ " + LANG.PUMP_ON, callback_data="pumpon"),
        ],
        [InlineKeyboardButton("⬅️ " + LANG.BACK, callback_data="pumpstat")],
    ]
)


pumponmenu = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🛑 " + LANG.PUMP_OFF, callback_data="pumpoff"),
            InlineKeyboardButton("🔄 " + LANG.REFRESH, callback_data="refresh"),
        ],
        [
            InlineKeyboardButton("🤖 " + LANG.BOT_PRED, callback_data="bot"),
        ],
        [InlineKeyboardButton("⬅️ " + LANG.BACK, callback_data="back")],
    ]
)

pumpoffmenu = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("✅ " + LANG.PUMP_ON, callback_data="pumpon"),
            InlineKeyboardButton("🔄 " + LANG.REFRESH, callback_data="refresh"),
        ],
        [
            InlineKeyboardButton("🤖 " + LANG.BOT_PRED, callback_data="bot"),
        ],
        [InlineKeyboardButton("⬅️ " + LANG.BACK, callback_data="back")],
    ]
)


def backkey(callback):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("⬅️ " + LANG.BACK, callback_data=callback)]]
    )


settingskey = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("⬅️ " + LANG.LANG, callback_data="lang")],
        [InlineKeyboardButton("🛑 " + LANG.QUIT, callback_data="exit")],
    ]
)

languageskey = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("English ", callback_data="eng"),
            InlineKeyboardButton("తెలుగు", callback_data="tel"),
        ],
        [
            InlineKeyboardButton("தமிழ்", callback_data="tam"),
            InlineKeyboardButton("हिन्दी", callback_data="hin"),
        ],
        [InlineKeyboardButton("🛑 " + LANG.QUIT, callback_data="exit")],
    ]
)
