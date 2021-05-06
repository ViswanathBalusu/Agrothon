#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   tamil.py
@Path    :   agrothon/tgbot/translations/
@Time    :   2021/05/4
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.1
@Contact :   ckvbalusu@gmail.com
@Desc    :   Tamil translations
"""


class Language(object):
    # Main Menu
    MAIN_MENU = "<b>Main Menu</b>"

    # Open Weather
    WEATHER_FETCH = "Fetching Details Please Wait"
    WEATHER = """
<b>📍 Location :</b><code> {}</code>
<b>🌡️ Temperature : </b><code>{} °C</code>
<b>💨 Pressure : </b><code>{} Pa</code>
<b>💧 Humidity : </b><code>{} g.m-3</code>
<b>⛅ Weather : </b><code>{}</code>
"""
    WEATHER_ERR = "<b>Error Occoured, Response : <code>{}</code> </b>"

    # Button Callbacks

    MOISTURE = "Moisture"
    HUMIDITY = "Humidity"
    TEMPERATURE = "Temparature"
    RAIN = "Rainfall Status"
    PUMP_STATUS = "Pump Status"
    COMPLETE_INFO = "Complete info"
    QUIT = "Quit"
    PUMP_OFF = "Switch OFF"
    PUMP_ON = "Switch On"
    BACK = "Back"
    BOT_PRED = "Turn on Bot Predicton"
    REFRESH = "Refresh Status"

    # Thing Speak Data

    MOISTURE_RESP = """
<b>Moisture 💧 in the Soil : </b><code> {}%</code>

"""
    HUMID_RESP = """
<b>Humidity ⛅ in the Field : </b><code> {}%</code>

"""
    TEMPE_RESP = """
<b>Temparature 🌡️ in the Field : </b><code> {}°C</code>

"""
    RAIN_YES_RESP = """
<b>It's raining 🌧️ out ther</b>

"""
    RAIN_NO_RESP = """
<b>It's not raining 🌞</b>

"""
    COMPLETE_RESP = """
<b>💧 Moisture : </b><code> {}%</code>
<b>⛅ Humidity : </b><code> {}%</code>
<b>🌡️ Temparature : </b><code> {}°C</code>
<b>🌧️ Is Raining : </b><code> {}</code>

"""
    # Pump
    PUMP_SWITCHED_ON = """
<b>The Pump is Running</b>
Switched ON by <code> {}</code>
Last Check : <code> {}</code>
"""

    PUMP_SWITCHED_OFF = """
<b>The Pump is OFF</b>
Switched OFF by <code> {}</code>
Last Check : <code> {}</code>
"""

    BOT_ACTIVATED = """<b>🤖 Bot mode is Activated </b>
Now you can sit back and relax 🛏️ and let 🤖 Bot manage your farm 🚜
"""
    PUMP_BTN_ON = """
<b> ✅ Running Status Changed </b>
Switched ON by<code> User</code>
"""

    PUMP_BTN_OFF = """
<b> ✅ Running Status Changed </b>
Switched OFF by<code> User</code>
"""

    SETTINGS = "⚙️ Settings ⚙️"
    LANG = "🌐 Change Language 🌐"
    SELECT_LANG = "Select Preferred Language"
    LANG_CHANGED = "Language has been Changed to English"
    OBJECTS = "Objects"
    DET_NO = "Found"
    ALERT_MESSAGE = """
<b>Intruders has been Detected </b>
<b>Detected at</b> : <code> {}</code>
<b>No of objects detected</b> : <code> {}</code>
<b>No of people detected</b> : <code> {}</code>

<pre>{}</pre>
"""
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
    MONTH = "Month"
    RAINFALL = "Rainfall(in {})"
    RAIN_PREDICT = """
<b>Rainfall predictions for this year</b>
<b>State </b>: <code> {}</code>
<b>District </b>: <code> {}</code>

<pre>{}</pre>
"""
    RAIN_PREDICT_ERR = """
Error while
"""
