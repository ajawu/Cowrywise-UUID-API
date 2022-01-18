#!/bin/sh
poetry export --without-hashes > requirements.txt
docker build -t cowrywise-uuid-api:v0.1 .
docker run -it -d --name=uuid-api -p 8000:8000 cowrywise-uuid-api:v0.1
