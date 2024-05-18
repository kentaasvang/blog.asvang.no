./venv/bin/uvicorn --host "127.0.0.1" --port 5005 --reload --reload-dir "templates" --workers 2 --log-level debug app:app
