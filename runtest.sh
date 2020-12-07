#!/bin/sh

echo "Building + Running containers"

docker-compose build 
docker-compose up -d 

echo "Creating + Seeding DB"
docker-compose exec api python manage.py recreate_db
docker-compose exec api python manage.py seed_db

echo "Running tests with coverage and html report"
docker-compose exec api python -m pytest "src/tests" -p no:warnings --cov="src" --cov-report html


echo "Linting"
docker-compose exec api flake8 src

echo "Running + Editing using Black"
docker-compose exec api black src 