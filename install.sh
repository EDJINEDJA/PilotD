#!/usr/bin/env bash
# exit on error
#gunicorn index:app --bind 0.0.0.0:8080 --timeout 1000 --worker-class uvicorn.workers.UvicornWorker
set -o errexit
pip install --upgrade pip
pip install -r requirements.txt
