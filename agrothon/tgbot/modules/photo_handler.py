#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   photo_handler.py
@Path    :   agrothon/tgbot/modules/
@Time    :   2021/05/6
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.3
@Contact :   ckvbalusu@gmail.com
@Desc    :   Pyrogram Photo Filter to detect objects
"""
import os
import uuid

from prettytable import PrettyTable

from agrothon import LANG

from ..Client import AgroBot, filters
from ..helpers.apiserverhelper import upload_file_to_api


@AgroBot.on_message(filters.photo)
async def photo_detect(client, message):
    temp_uuid = str(uuid.uuid4())
    path = f"tmp/{temp_uuid}.jpg"
    init_msg = await message.reply_text("Downloading from telegram")
    downloaded_file = await client.download_media(message=message, file_name=path)
    if os.path.exists(downloaded_file):
        proc_message = await init_msg.edit_text(
            f"Downloaded, Detecting Objects Please wait..."
        )
        status, image = await upload_file_to_api(downloaded_file)
        if status:
            pt = PrettyTable([LANG.OBJECTS, LANG.DET_NO])
            pt.align[LANG.OBJECTS] = "l"
            pt.align[LANG.DET_NO] = "c"
            pt.padding_width = 0
            pt.format = True
            # only_h = image["only_humans"]
            image_url = image["image_url"]
            detections = image["detections"]
            hums = image["humans"]
            tot_dets = image["no_of_detections"]
            for obj in detections:
                pt.add_row([obj["type"], obj["count"]])
            await proc_message.delete()
            await message.reply_photo(
                photo=image_url,
                quote=True,
                caption=LANG.IMAGE_MESSAGE.format(tot_dets, hums, pt),
                parse_mode="html",
            )
        else:
            await message.reply_text(text=LANG.ERR_IMAGE_RESPONSE)
