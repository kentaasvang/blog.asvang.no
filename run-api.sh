#!/bin/bash
./venv/bin/python3.12 -m uvicorn api.api:app --host "127.0.0.1" --port 5001 --reload --reload-dir "./api/"
