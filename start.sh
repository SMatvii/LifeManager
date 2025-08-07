#!/bin/bash
set -e

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Navigating to Django project..."
cd finassistant

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate

echo "Starting gunicorn server..."
gunicorn finassistant.wsgi:application --bind 0.0.0.0:$PORT
