#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   telugu.py
@Path    :   agrothon/tgbot/translations/
@Time    :   2021/05/24
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.2.7
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
    MOISTURE_SENSOR = """<b>💧 మట్టిలో తేమ (సెన్సార్ {}): </b><code> {}%</code>\n"""
    MOISTURE_RESP = """<b>🕒 చివరిసారి నవీకరించబడింది : </b><code> {}</code>
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
    COMPLETE_MOISTURE = """<b>💧 తేమ (సెన్సార్ {}): </b><code> {}%</code>\n"""
    COMPLETE_RESP = """<b>⛅ తడి: </b><code> {}%</code>
<b>🌡️ ఉష్ణోగ్రత : </b><code> {}°C</code>
<b>⛏️ పంప్ స్థితి ఎలా ఉండాలి (సెన్సార్ {}): </b><code> {}</code>
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
    LANG_CHANGED = "భాష మారుతోంది, దయచేసి వేచి ఉండండి"
    OBJECTS = "వస్తువులు"
    DET_NO = "కనుగొన్నారు"
    ALERT_MESSAGE = """
<b>చొరబాటుదారులు కనుగొనబడ్డారు </b>
<b>కనుగొనబడిన సమయం</b> : <code> {}</code>
<b>వస్తువుల సంఖ్య</b> : <code> {}</code>
<b>వ్యక్తుల సంఖ్య</b> : <code> {}</code>

<pre>{}</pre>
"""
    MONTHS = [
        "ఏప్రిల్",
        "మే",
        "జూన్",
        "జూలై",
        "ఆగస్టు",
        "సెప్టెంబర్",
        "అక్టోబర్",
        "నవంబర్",
        "డిసెంబర్",
    ]
    MONTH = "నెల"
    RAINFALL = "వర్షపాతం ({} లో)"
    RAIN_PREDICT = """
<b> ఈ సంవత్సరానికి వర్షపాతం అంచనాలు </b>
<b> రాష్ట్రం </b>: <code> {} </code>
<b> జిల్లా </b>: <code> {} </code>

<pre>{}</pre>
"""
    RAIN_PREDICT_ERR = """
ప్రిడిక్షన్ చేస్తున్నప్పుడు లోపం
"""
    IMAGE_MESSAGE = """
<b>వస్తువులు కనుగొనబడ్డాయి</b>
<b>వస్తువుల సంఖ్య</b> : <code> {}</code>
<b>వ్యక్తుల సంఖ్య</b> : <code> {}</code>

<pre>{}</pre>
"""
    ERR_IMAGE_RESPONSE = """
<b>చిత్రంలో ఏమీ కనుగొనబడలేదు</b>
"""
    PRED_PUMP_OFF = "ఆఫ్"
    PRED_PUMP_ON = "ఆన్"
    STATS = """
<b> సమయము: </b> <code> {} </code>
<b> డిస్క్ స్థలం: </b> <code> {} </code>
<b> ఉపయోగించబడింది: </b> <code> {} </code>
<b> ఉచిత: </b> <code> {} </code>
<b> CPU వినియోగం: </b> <code> {}% </code>
<b> RAM వినియోగం: </b> <code> {}% </code>
<b> అప్‌లోడ్ చేయబడింది: </b> <code> {} </code>
<b> డౌన్‌లోడ్ చేయబడింది: </b> <code> {} </code>
"""
    DL_TG = "టెలిగ్రామ్ నుండి డౌన్‌లోడ్ అవుతోంది"
    PROC_IMAGE = "డౌన్‌లోడ్ చేయబడింది, వస్తువులను గుర్తించడం దయచేసి వేచి ఉండండి ..."
    RESTART = "పునఃప్రారంభించి, దయచేసి వేచి ...."
    RESTART_DONE = "విజయవంతంగా పునఃప్రారంభం!"
    RESTART_CALLBACK = "పునఃప్రారంభించండి"
    WEATHER_FETCHING = "వాతావరణం పొందడం, దయచేసి వేచి ఉండండి"
    HELP_MESSAGE = """
<code>/{} </code>: మీ నగరం యొక్క వాతావరణ స్థితి
<code>/{} </code>: మీ ప్రాంతం యొక్క వర్షపాతాన్ని అంచనా వేయండి
<code>/{} </code>: మీ ఫీల్డ్ స్థితిని పొందండి మరియు మీ పంపుని నిర్వహించండి
<code>/{} </code>: మీ బొట్ యొక్క సెట్టింగులను మార్చండి
<code>/{} </code>: సర్వర్ గణాంకాలను పొందండి
<code>/{} </code>: పింగ్‌ను తనిఖీ చేయండి
<code>/{} </code>: సర్వర్ యొక్క లాగ్ పొందండి
<code>/{} </code>: సర్వర్‌ను పున ప్రారంభించండి
<code>/{} </code>: ఈ సందేశాన్ని పొందడానికి

<code> చిత్రంలోని వస్తువులను గుర్తించడానికి చిత్రాన్ని పంపండి </code>
"""
    START = """
హే, నేను <code> అగ్రోథాన్ </code>

  - మీరు మీ పొలాన్ని పర్యవేక్షించవచ్చు
  - పంప్ స్థితిని ఆన్ లేదా ఆఫ్‌కు మార్చండి
  - వాతావరణం పొందండి
  - చిత్రంలోని వస్తువులను గుర్తించండి
  - మీ ప్రాంతానికి వర్షపాతాన్ని అంచనా వేయండి
"""
    PING_START = "పింగ్ ప్రారంభమవుతుంది"
    PING_FINAL = "కొలిచిన పింగ్ : {}"
    LANG_SET = "విజయవంతంగా భాషను తెలుగుగా మార్చారు"
    PUMP_STATUS_ON = "ఆన్"
    PUMP_STATUS_OFF = "ఆఫ్"
