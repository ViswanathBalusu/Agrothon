#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   database.py
@Path    :   agrothon/server/helpers/
@Time    :   2021/05/5
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.2
@Contact :   ckvbalusu@gmail.com
@Desc    :   database module
"""

import logging

from motor.motor_asyncio import AsyncIOMotorClient

LOGGER = logging.getLogger(__name__)


class MongoClient:
    def __init__(self, DB_URL):
        self.DataBaseClient = None
        self.DB_URL = DB_URL

    async def get_db(self):
        """Return Database"""
        LOGGER.debug("Getting Database")
        return self.DataBaseClient.Agrothon

    async def connect_db(self):
        """Create database connection."""
        LOGGER.info("Connecting to database")
        self.DataBaseClient = AsyncIOMotorClient(self.DB_URL)

    async def close_mongo_connection(self):
        """Close database connection."""
        LOGGER.info("Closing database connection")
        self.DataBaseClient.close()
