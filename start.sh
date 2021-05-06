#!/bin/bash
uvicorn --host 0.0.0.0 --port 10808 agrothon.API:Agrothon &
python3 -m agrothon