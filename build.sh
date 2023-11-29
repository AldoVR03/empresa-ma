#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
pip install -r requirements.txt
pip install django-widget-tweaks
pip install whitenoise
#---
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate