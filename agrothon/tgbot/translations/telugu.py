#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   telugu.py
@Path    :   agrothon/tgbot/translations/
@Time    :   2021/05/4
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.1
@Contact :   ckvbalusu@gmail.com
@Desc    :   Telugu translations
"""


class Language(object):
    # Main Menu
    MAIN_MENU = "<b>ప్రధాన మెనూ</b>"

    # Open Weather
    WEATHER_FETCH = "వివరాలు శోధిస్తోంది దయచేసి వేచి ఉండండి"
    WEATHER = """
<b>📍 స్థానం :</b><code> {}</code>
<b>🌡️ ఉష్ణోగ్రత : </b><code>{} °C</code>
<b>💨 ప్రెజర్ : </b><code>{} Pa</code>
<b>💧 తేమ : </b><code>{} g.m-3</code>
<b>⛅ వాతావరణం : </b><code>{}</code>
"""
    WEATHER_ERR = "<b>లోపం సంభవించింది, ప్రతిస్పందన: <code>{}</code> </b>"

    # Button Callbacks

    MOISTURE = "తేమ"
    HUMIDITY = "తడి"
    TEMPERATURE = "ఉష్ణోగ్రత"
    RAIN = "వర్షపాతం స్థితి"
    PUMP_STATUS = "పంప్ స్థితి"
    COMPLETE_INFO = "పూర్తి సమాచారం"
    QUIT = "క్విట్"
    PUMP_OFF = "ఆపి వేయి"
    PUMP_ON = "స్విచ్ ఆన్"
    BACK = "వెనుక మెను"
    BOT_PRED = "బొట్ ప్రిడిక్షన్ ఆన్ చేయండి"
    REFRESH = "స్థితిని రిఫ్రెష్"

    # Thing Speak Data

    MOISTURE_RESP = """
<b>💧 మట్టిలో తేమ : </b><code> {}%</code>
<b>🕒 చివరిసారి నవీకరించబడింది : </b><code> {}</code>
<b>🕒 చివరి తనిఖీ : </b><code> {}</code>
"""
    HUMID_RESP = """
<b>⛅ పొలంలో తేమ : </b><code> {}%</code>
<b>🕒 చివరిసారి నవీకరించబడింది : </b><code> {}</code>
<b>🕒 చివరి తనిఖీ : </b><code> {}</code>
"""
    TEMPE_RESP = """
<b>🌡️ పొలంలో ఉష్ణోగ్రత : </b><code> {}°C</code>
<b>🕒 చివరిసారి నవీకరించబడింది: </b><code> {}</code>
<b>🕒 చివరి తనిఖీ: </b><code> {}</code>
"""
    RAIN_YES_RESP = """
<b>పొలంలో వర్షం పడుతోంది 🌧️</b>

"""
    RAIN_NO_RESP = """
<b>పొలంలో వర్షం పడటం లేదు 🌞</b>

"""
    COMPLETE_RESP = """
<b>💧 తేమ : </b><code> {}%</code>
<b>⛅ తడి: </b><code> {}%</code>
<b>🌡️ ఉష్ణోగ్రత : </b><code> {}°C</code>
<b>⛏️ పంప్ స్థితి ఎలా ఉండాలి : </b><code> {}</code>
<b>🕒 చివరిసారి నవీకరించబడింది : </b><code> {}</code>
<b>🕒 చివరి తనిఖీ : </b><code> {}</code>
"""
    # Pump
    PUMP_SWITCHED_ON = """
<b>పంప్ ఆన్లో ఉంది</b>
<code>{} </code> ద్వారా మార్చబడింది
చివరి తనిఖీ : <code> {}</code>
"""

    PUMP_SWITCHED_OFF = """
<b>పంప్ ఆఫ్లో ఉంది</b>
<code>{} </code> ద్వారా స్విచ్ ఆఫ్ చేయబడింది
చివరి తనిఖీ : <code> {}</code>
"""

    BOT_ACTIVATED = """<b>🤖 బాట్ మోడ్ సక్రియం చేయబడింది </b>
ఇప్పుడు మీరు తిరిగి కూర్చుని విశ్రాంతి తీసుకోవచ్చు 🛏️ మరియు మీ 🤖 బొట్ మీ పొలాన్ని నిర్వహించడానికి అనుమతించండి 🚜
"""
    PUMP_BTN_ON = """
<b> ✅ రన్నింగ్ స్థితి మార్చబడింది</b>
<code>User </code> ద్వారా మార్చబడింది
"""

    PUMP_BTN_OFF = """
<b> ✅ రన్నింగ్ స్థితి మార్చబడింది </b>
<code>User </code> ద్వారా మార్చబడింది
"""
    LANG = "🌐 భాష మార్చు 🌐"
    SETTINGS = "⚙️ సెట్టింగులు ⚙️"
    SELECT_LANG = "ప్రాధాన్య భాష"
    LANG_CHANGED = "భాషను తెలుగుగా మార్చారు"
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
    PRED_PUMP_OFF = "ఆఫ్"
    PRED_PUMP_ON = "ఆన్"
