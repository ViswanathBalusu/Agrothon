#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   hindi.py
@Path    :   agrothon/tgbot/translations/
@Time    :   2021/05/4
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.1
@Contact :   ckvbalusu@gmail.com
@Desc    :   Hindi translations
"""


class Language(object):
    # Main Menu
    MAIN_MENU = "<b>मुख्य मेन्यू</b>"

    # Open Weather
    WEATHER_FETCH = "कृपया प्रतीक्षा करें जानकारी के लिये...."
    WEATHER = """
<b>📍 स्थान :</b><code> {}</code>
<b>🌡️ तापमान : </b><code>{} °C</code>
<b>💨 दबाव/प्रिशर : </b><code>{} Pa</code>
<b>💧 आर्द्रता : </b><code>{} g.m-3</code>
<b>⛅ मौसम : </b><code>{}</code>
"""
    WEATHER_ERR = "<b>गड़बड़ी हुइ हे, प्रतिक्रिया : <code>{}</code> </b>"

    # Button Callbacks

    MOISTURE = "नमी"
    HUMIDITY = "आर्द्रता"
    TEMPERATURE = "तापमान"
    RAIN = "वर्षा स्थिति"
    PUMP_STATUS = "पंप स्थिति"
    COMPLETE_INFO = "पूर्ण जानकारी"
    QUIT = "बंद करे"
    PUMP_OFF = "स्विच ऑफ"
    PUMP_ON = "स्विच वन"
    BACK = "पीछे"
    BOT_PRED = "बौट पूर्वानुमान को चालू करें"
    REFRESH = "रिफ्रेश स्थिति"

    # Thing Speak Data

    MOISTURE_RESP = """
<b>💧 मिट्टी में नमी : </b><code> {}%</code>
<b>🕒 अंतिम बार अपडेट किया गया: </b><code> {}</code>
<b>🕒 अंतिम बार देखा गया था: </b><code> {}</code>
"""
    HUMID_RESP = """
<b>⛅ मैदान में आर्द्रता : </b><code> {}%</code>
<b>🕒 अंतिम बार अपडेट किया गया: </b><code> {}</code>
<b>🕒 अंतिम बार देखा गया था: </b><code> {}</code>
"""
    TEMPE_RESP = """
<b>मैदान में तापमान🌡️ : </b><code> {}°C</code>
<b>🕒 अंतिम बार अपडेट किया गया: </b><code> {}</code>
<b>🕒 अंतिम बार देखा गया था: </b><code> {}</code>
"""
    RAIN_YES_RESP = """
<b>वहां बारिश🌧️ हो रही है</b>

"""
    RAIN_NO_RESP = """
<b>बारिश नहीं हो रही है 🌞</b>

"""
    COMPLETE_RESP = """
<b>💧 नमी : </b><code> {}%</code>
<b>⛅ आर्द्रता : </b><code> {}%</code>
<b>🌡️ तापमान : </b><code> {}°C</code>
<b>⛏️ पंप होना चाहिए : </b><code> {}</code>
<b>🕒 अंतिम बार अपडेट किया गया: </b><code> {}</code>
<b>🕒 अंतिम बार देखा गया था: : </b><code> {}</code>

"""
    # Pump
    PUMP_SWITCHED_ON = """
<b>पंप चल रहा है</b>
स्विच वन किया <code> {}</code>
अंतिम जांच : <code> {}</code>
"""

    PUMP_SWITCHED_OFF = """
<b>पंप बंद है</b>
स्विच ऑफ किया  <code> {}</code>
अंतिम जांच : <code> {}</code>
"""

    BOT_ACTIVATED = """<b>🤖 बॉट मोड सक्रिय है </b>
अब आप आराम से बैठ सकते हैं 🛏️ और 🤖 बॉट को अपने खेत को संभालने दें 🚜
"""
    PUMP_BTN_ON = """
<b> ✅ चलने का स्थिति बदल दिया </b>
स्विच वन किया <code> User</code>
"""

    PUMP_BTN_OFF = """
<b> ✅ चलने का स्थिति बदल दिया </b>
स्विच ऑफ किया <code> User</code>
"""

    SETTINGS = "⚙️ सेटिंग ⚙️"
    LANG = "🌐 भाषा बदलें 🌐"
    SELECT_LANG = "पसंदीदा भाषा का चयन करें"
    LANG_CHANGED = "Language has been Changed to हिंदी"
    OBJECTS = "वस्तुओं"
    DET_NO = "मिल गया"
    ALERT_MESSAGE = """
<b>घुसपैठियों का पता चला है </b>
<b>येहा पता चला हे</b> : <code> {}</code>
<b>वस्तुओं की संख्या पता लगाना</b> : <code> {}</code>
<b>लोगों की संख्या पता लगाना</b> : <code> {}</code>

<pre>{}</pre>
"""
    MONTHS = [
        "अप्रैल",
        "मई",
        "जून",
        "जुलाई",
        "अगस्त",
        "सितम्बर",
        "अक्टूबर",
        "नवम्बर",
        "दिसम्बर",
    ]
    MONTH = "महीना"
    RAINFALL = "वर्षा(in {})"
    RAIN_PREDICT = """
<b>वर्षा पूर्वानुमान इस साल के लिए</b>
<b>राज्य </b>: <code> {}</code>
<b>जिला </b>: <code> {}</code>

<pre>{}</pre>
"""
    RAIN_PREDICT_ERR = """
गड़बड़ी जबकि
"""
    IMAGE_MESSAGE = """
<b>वस्तुओं या लोगों का पता चला है </b>
<b>वस्तुओं की संख्या पता लगाना</b> : <code> {}</code>
<b>लोगों की संख्या पता लगाना</b> : <code> {}</code>

<pre>{}</pre>
"""
    ERR_IMAGE_RESPONSE = """
<b>छवि में कुछ भी नहीं मिला</b>
"""
    PRED_PUMP_OFF = "ऑफ"
    PRED_PUMP_ON = "वन"
