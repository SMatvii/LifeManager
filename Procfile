web: cd finassistant && python manage.py collectstatic --noinput && python manage.py migrate && gunicorn finassistant.wsgi --host 0.0.0.0 --port $PORT
