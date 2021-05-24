#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   english.py
@Path    :   agrothon/tgbot/translations/
@Time    :   2021/05/24
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.2.7
@Contact :   ckvbalusu@gmail.com
@Desc    :   English translations
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
    WEATHER_ERR = "<b>Error Occoured</b>"

    # Button Callbacks

    MOISTURE = "Moisture"
    HUMIDITY = "Humidity"
    TEMPERATURE = "Temperature"
    RAIN = "Rainfall Status"
    PUMP_STATUS = "Pump Status"
    COMPLETE_INFO = "Complete info"
    QUIT = "Quit"
    PUMP_OFF = "Switch OFF"
    PUMP_ON = "Switch On"
    BACK = "Back"
    BOT_PRED = "Turn on Bot Prediction"
    REFRESH = "Refresh Status"

    MOISTURE_SENSOR = """<b>💧 Moisture in the Soil (Sensor {}): </b><code> {}%</code>\n"""
    MOISTURE_RESP = """<b>🕒 Last Updated at: </b><code> {}</code>
<b>🕒 Last Read at: </b><code> {}</code>
"""
    HUMID_RESP = """
<b>⛅ Humidity in the Field : </b><code> {}%</code>
<b>🕒 Last Updated at: </b><code> {}</code>
<b>🕒 Last Read at: </b><code> {}</code>
"""
    TEMPE_RESP = """
<b>🌡️ Temparature in the Field : </b><code> {}°C</code>
<b>🕒 Last Updated at: </b><code> {}</code>
<b>🕒 Last Read at: </b><code> {}</code>
"""
    RAIN_YES_RESP = """
<b>It's raining 🌧️ out there</b>

"""
    RAIN_NO_RESP = """
<b>It's not raining 🌞</b>

"""
    COMPLETE_MOISTURE = """<b>💧 Moisture (Sensor {}): </b><code> {}%</code>\n"""
    COMPLETE_RESP = """<b>⛅ Humidity : </b><code> {}%</code>
<b>🌡️ Temperature : </b><code> {}°C</code>
<b>⛏️ Pump Should be (by Sensor {}): </b><code> {}</code>
<b>🕒 Last Updated at: </b><code> {}</code>
<b>🕒 Last Read at: </b><code> {}</code>
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
    LANG_CHANGED = "Changing Language, Please wait..."
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
    IMAGE_MESSAGE = """
<b>Objects has been Detected </b>
<b>No of objects detected</b> : <code> {}</code>
<b>No of people detected</b> : <code> {}</code>

<pre>{}</pre>
"""
    ERR_IMAGE_RESPONSE = """
<b>Nothing  Found in the image</b>
"""
    PRED_PUMP_OFF = "Off"
    PRED_PUMP_ON = "On"
    STATS = """
<b>Uptime :</b><code> {}</code>
<b>Disk Space :</b><code> {}</code>
<b>Used :</b><code> {}</code>
<b>Free :</b><code> {}</code>
<b>CPU Usage :</b><code> {}%</code>
<b>RAM :</b><code> {}%</code>
<b>Uploaded :</b><code> {}</code>
<b>Downloaded :</b><code> {}</code>
"""
    DL_TG = "Downloading from Telegram"
    PROC_IMAGE = "Downloaded, Detecting Objects please wait..."
    RESTART = "Restarting, please wait...."
    RESTART_DONE = "Restarted Successfully!"
    RESTART_CALLBACK = "Restart"
    WEATHER_FETCHING = "Fetching Weather, Please Wait"
    HELP_MESSAGE = """
<code>/{}</code> : Weather Status of your City
<code>/{}</code> : Predict rainfall of your region
<code>/{}</code> : Get your field status and manage your pump
<code>/{}</code> : Change settings of your Bot
<code>/{}</code> : Get the server stats
<code>/{}</code> : Check ping
<code>/{}</code> : Get the log of the server
<code>/{}</code> : Restart the server
<code>/{}</code> : To get this message

<code>To detect objects in an image just send the image</code>
"""
    START = """
Hey, I am <code>Agrothon</code>

 - you can monitor your farm
 - Change pump status  to on or off
 - Get weather
 - Detect Objects in an image
 - Predict rainfall for your region
"""
    PING_START = "Starting Ping"
    PING_FINAL = "Measured Ping : {}"
    LANG_SET = "English is successfully set as preferred language"
    PUMP_STATUS_ON = "ON"
    PUMP_STATUS_OFF = "OFF"
