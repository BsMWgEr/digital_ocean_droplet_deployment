#!/bin/bash
APP_PORT=${PORT:-8000}
cd /app/
/opt/venv/bin/python manage.py migrate
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm change_entrypoint_sh_.wsgi:application --bind "0.0.0.0:${APP_PORT}"