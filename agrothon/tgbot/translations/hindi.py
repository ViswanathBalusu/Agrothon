#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   hindi.py
@Path    :   agrothon/tgbot/translations/
@Time    :   2021/05/24
@Author  :   github.com/xavierxross
@Version :   1.2.7
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
    MOISTURE_SENSOR = """<b>💧 मिट्टी में नमी (सेंसर {}): </b><code> {}%</code>\n"""
    MOISTURE_RESP = """<b>🕒 अंतिम बार अपडेट किया गया: </b><code> {}</code>
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
    COMPLETE_MOISTURE = """<b>💧 नमी (सेंसर {}): </b><code> {}%</code>\n"""
    COMPLETE_RESP = """<b>⛅ आर्द्रता : </b><code> {}%</code>
<b>🌡️ तापमान : </b><code> {}°C</code>
<b>⛏️ पंप होना चाहिए (सेंसर {}): </b><code> {}</code>
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
    LANG_CHANGED = "भाषा बदलने की प्रतीक्षा करें"
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
    STATS = """
<b>अपटाइम:</b><code> {}</code>
<b>डिस्क स्थान :</b><code> {}</code>
<b>प्रयुक्त :</b><code> {}</code>
<b>निःशुल्क :</b><code> {}</code>
<b>CPU उपयोग:</b><code> {}%</code>
<b>RAM :</b><code> {}%</code>
<b>अपलोड किया गया:</b><code> {}</code>
<b>डाउनलोड किया गया:</b><code> {}</code>
"""
    DL_TG = "टेलीग्राम से डाउनलोड करना"
    PROC_IMAGE = "डाउनलोड किया गया, वस्तुओं का पता लगाना कृपया प्रतीक्षा करें..."
    RESTART = "पुनः प्रारंभ हो रहा है, कृपया प्रतीक्षा करें...."
    RESTART_DONE = "सफलतापूर्वक पुनरारंभ किया गया!"
    RESTART_CALLBACK = "पुनः आरंभ करें"
    WEATHER_FETCHING = "मौसम आ रहा है, कृपया प्रतीक्षा करें"
    HELP_MESSAGE = """
<code>/{}</code> : आपके शहर की मौसम स्थिति
<code>/{}</code> : अपने क्षेत्र की वर्षा की भविष्यवाणी करें
<code>/{}</code> : अपने क्षेत्र की स्थिति प्राप्त करें और अपने पंप का प्रबंधन करें
<code>/{}</code> : अपने बॉट की सेटिंग बदलें
<code>/{}</code> : सर्वर आँकड़े प्राप्त करें
<code>/{}</code> : पिंग चेक करें
<code>/{}</code> : सर्वर का लॉग प्राप्त करें
<code>/{}</code> : सर्वर को पुनरारंभ करें
<code>/{}</code> : यह संदेश पाने के लिए

<code>किसी इमेज में ऑब्जेक्ट का पता लगाने के लिए बस इमेज भेजें</code>
"""
    START = """
अरे, मैं हूं <code>एग्रोथॉन</code>

  - आप अपने खेत की निगरानी कर सकते हैं
  - पंप की स्थिति को चालू या बंद में बदलें
  - मौसम प्राप्त करें
  - एक छवि में वस्तुओं का पता लगाएं
  - अपने क्षेत्र के लिए वर्षा की भविष्यवाणी करें
"""
    PING_START = "पिंग शुरू करना"
    PING_FINAL = "मापा पिंग : {}"
    LANG_SET = "हिंदी को पसंदीदा भाषा के रूप में सेट करना सफल रहा"
    PUMP_STATUS_ON = "चालू"
    PUMP_STATUS_OFF = "बंद"
