#!/bin/bash
agroserver & # FastAPI API Server
sleep 5
caddy reverse-proxy --from :"$API_PORT" --to unix//usr/agrothon.sock & # Caddy Reverse Proxy