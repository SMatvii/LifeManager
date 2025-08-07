FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gettext \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/finassistant

RUN python manage.py collectstatic --noinput

EXPOSE $PORT

CMD cd /app/finassistant && gunicorn finassistant.wsgi:application --bind 0.0.0.0:$PORT