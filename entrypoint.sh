#!/bin/bash
set -e

echo "Installing Python dependencies..."
pip install --no-cache-dir -r requirements.txt

echo "Changing to Django directory..."
cd finassistant

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running database migrations..."
python manage.py migrate

echo "Starting Gunicorn server..."
exec python -m gunicorn finassistant.wsgi:application --bind 0.0.0.0:$PORT
