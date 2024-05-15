#!/bin/bash
python3.12 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python manage.py makemigrations
venv/bin/python manage.py migrate
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=your@email.com
export DJANGO_SUPERUSER_PASSWORD=pwd
venv/bin/python manage.py createsuperuser --no-input
venv/bin/python manage.py loaddata initial_parties.json
venv/bin/python manage.py loaddata initial_gifts.json
venv/bin/python manage.py loaddata initial_guests.json
venv/bin/python manage.py tailwind download_cli
cp .env.dist .env