#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   rainfall.py
@Path    :   agrothon/tgbot/modules/
@Time    :   2021/05/8
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.1.0
@Contact :   ckvbalusu@gmail.com
@Desc    :   General utils module for Telegram bot
"""

from ..Client import AgroBot, filters
from agrothon import SERVER_TIME, LANG, STATS_COMMAND, LOG_COMMAND, HELP_COMMAND
import psutil
import shutil
import time
from typing import Optional


def get_readable_file_size(size_in_bytes) -> Optional[str]:
    size_units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    if size_in_bytes is None:
        return '0B'
    index = 0
    while size_in_bytes >= 1024:
        size_in_bytes /= 1024
        index += 1
    try:
        return f'{round(size_in_bytes, 2)}{size_units[index]}'
    except IndexError:
        return None


def get_readable_time(seconds: int) -> str:
    result = ''
    (days, remainder) = divmod(seconds, 86400)
    days = int(days)
    if days != 0:
        result += f'{days}d'
    (hours, remainder) = divmod(remainder, 3600)
    hours = int(hours)
    if hours != 0:
        result += f'{hours}h'
    (minutes, seconds) = divmod(remainder, 60)
    minutes = int(minutes)
    if minutes != 0:
        result += f'{minutes}m'
    seconds = int(seconds)
    result += f'{seconds}s'
    return result


@AgroBot.on_message(filters.command([STATS_COMMAND]))
async def stats(client, message):
    current_time = get_readable_time((time.time() - SERVER_TIME))
    total, used, free = shutil.disk_usage('.')
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    cpu_usage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
    rec = get_readable_file_size(psutil.net_io_counters().bytes_recv)
    await message.reply_text(text=LANG.STATS.format(current_time, total, used, free, cpu_usage, memory, sent, rec))


@AgroBot.on_message(filters.command([LOG_COMMAND]))
async def send_log(client, message):
    await message.reply_document("Agrothon.txt")
