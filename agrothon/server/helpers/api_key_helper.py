#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   api_key_helper.py
@Path    :   agrothon/server/helpers/
@Time    :   2021/05/6
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.3
@Contact :   ckvbalusu@gmail.com
@Desc    :   API Key auth Checker Module
"""
import logging

from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyQuery

from agrothon import API_KEY

API_KEY_NAME = "api_key"
LOGGER = logging.getLogger(__name__)

api_key_query_auth = APIKeyQuery(name=API_KEY_NAME, auto_error=True)


async def verify_api_key(api_key_query: str = Security(api_key_query_auth)):
    if api_key_query != API_KEY:
        LOGGER.info("API Key Mismatch")
        LOGGER.debug(f"Wrong API Key used : {api_key_query}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )
