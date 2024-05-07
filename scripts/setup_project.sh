#!/bin/bash
python3.12 -m venv venv
source "$PWD/../venv/bin/python"
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata initial_parties.json
python manage.py loaddata initial_gifts.json
python manage.py loaddata initial_guests.json