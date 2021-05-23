#!/bin/bash
agroserver & # FastAPI API Server
sleep 30 # Wait for the Uvicorn Server to start
caddy run --config /Caddyfile # Start Caddy Reverse proxy
