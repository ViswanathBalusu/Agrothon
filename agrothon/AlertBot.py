#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   AlertBot.py
@Path    :   agrothon/
@Time    :   2021/05/8
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.1.0
@Contact :   ckvbalusu@gmail.com
@Desc    :   Intruder alert bot
"""
import time
import os
from prettytable import PrettyTable
from telegram.ext import Updater

from agrothon import ALERT_CHANNEL_ID, BOT_TOKEN, LANG

from .tgbot.helpers.apiserverhelper import get_image_url, get_image_uuids

tg = Updater(token=BOT_TOKEN)
AlertBot = tg.bot


def alerts_handler():
    while True:
        response = get_image_uuids()
        if response is not None:
            for image in response["image_data"]:
                pt = PrettyTable([LANG.OBJECTS, LANG.DET_NO])
                pt.align[LANG.OBJECTS] = "l"
                pt.align[LANG.DET_NO] = "c"
                pt.padding_width = 0
                only_h = image["only_humans"]
                image_url = get_image_url(image["uuid"])
                detections = image["detections"]
                hums = image["humans"]
                tot_dets = image["no_of_detections"]
                for obj in detections:
                    pt.add_row([obj["type"], obj["count"]])
                at = image["at"]
                try:
                    if not only_h:
                        AlertBot.sendPhoto(
                            chat_id=ALERT_CHANNEL_ID,
                            photo=image_url,
                            caption=LANG.ALERT_MESSAGE.format(at, tot_dets, hums, pt),
                            parse_mode="HTML",
                        )
                    else:
                        AlertBot.sendPhoto(
                            chat_id=ALERT_CHANNEL_ID,
                            photo=image_url,
                            caption=LANG.ALERT_MESSAGE.format(at, tot_dets, hums, pt),
                            parse_mode="HTML",
                            disable_notification=True,
                        )
                except Exception:
                    pass
        time.sleep(1)


def restart_check():
    if os.path.isfile(".restartfile"):
        with open(".restartfile") as f:
            chat_id, msg_id = map(int, f)
        AlertBot.edit_message_text(LANG.RESTART_DONE, chat_id, msg_id)
        os.remove(".restartfile")


def language_change_check():
    if os.path.isfile(".setlangfile"):
        with open(".setlangfile") as f:
            chat_id, msg_id = map(int, f)
        AlertBot.edit_message_text(LANG.LANG_SET, chat_id, msg_id)
        os.remove(".setlangfile")
