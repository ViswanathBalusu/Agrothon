#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Path    :   agrothon/tgbot/translations/
@Time    :   2021/05/5
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.2
@Contact :   ckvbalusu@gmail.com
@Desc    :   Language translations init
"""

from . import english, hindi, tamil, telugu


def setLang(lang):
    if lang == "telugu":
        _lang = telugu.Language()
    elif lang == "tamil":
        _lang = tamil.Language()
    elif lang == "hindi":
        _lang = hindi.Language()
    else:
        _lang = english.Language()
    return _lang
