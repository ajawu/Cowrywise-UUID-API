#!/bin/sh
docker build -t cowrywise_uuid_api:1.0 .
docker run -d -p 8000:8000 cowrywise_uuid_api:1.0 sh -c "python manage.py migrate"
