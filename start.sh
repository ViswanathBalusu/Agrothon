#!/bin/bash
uvicorn --host 0.0.0.0 --port $PORT agrothon.API:Agrothon &
python3 -m agrothon