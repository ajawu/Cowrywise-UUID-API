#!/bin/bash

set -e

echo "${0}: running migrations."
python manage.py migrate --noinput

gunicorn --reload --bind=0.0.0.0:8000 --timeout=82 --workers=3 cowrywise_uuid_api.wsgi:application