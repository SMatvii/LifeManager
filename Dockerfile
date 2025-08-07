FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gettext \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

COPY . .

EXPOSE $PORT

CMD ["bash", "entrypoint.sh"]