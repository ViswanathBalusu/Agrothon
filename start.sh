#!/bin/bash
agroserver & # FastAPI API Server
agrothon & # Telegram Bot
caddy reverse-proxy --from :"$API_PORT" --to unix//usr/agrothon.sock # Caddy Reverse Proxy