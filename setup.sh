#!/bin/sh

docker-compose build --no-cache
docker-compose up -d 
docker-compose exec api python manage.py recreate_db
docker-compose exec api python manage.py seed_db
docker-compose exec api python -m pytest "src/tests" -p no:warnings --cov="src" --cov-report html
