FROM python:3.12-slim

# Встановлюємо системні залежності
RUN apt-get update && apt-get install -y \
    gettext \
    libpq-dev \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо та встановлюємо Python залежності
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проект
COPY . .

# Відкриваємо порт
EXPOSE 8000

# Команда за замовчуванням (може бути перевизначена в docker-compose)
CMD ["sh", "-c", "cd finassistant && python manage.py runserver 0.0.0.0:8000"]