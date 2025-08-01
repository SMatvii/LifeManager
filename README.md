# LifeManager - Фінансовий помічник

<div align="center">
  <img src="finassistant/core/static/img/LifeManager.png" alt="LifeManager Logo" width="623" height="548">
</div>


[![Django CI](https://img.shields.io/badge/Django-CI-blue)](https://github.com/SMatvii/LifeManager/actions)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Django 5.2+](https://img.shields.io/badge/django-5.2+-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Сучасний веб-додаток для управління особистими фінансами та плануванням подій

## Особливості

- **Управління транзакціями**: Відстеження доходів та витрат з категоризацією
- **Аналітика**: Статистика витрат по категоріях та періодах
- **Планування подій**: Календар завдань з пріоритетами та дедлайнами
- **Профілі користувачів**: Персоналізація з аватарками
- **Безпечна авторизація**: Власна реєстрація + Google/GitHub OAuth
- **REST API**: Повноцінний API з Swagger документацією
- **Сучасний UI**: Адаптивний дизайн з Bootstrap 5

## Технологічний стек

- **Backend**: Django 5.2+ | Django REST Framework 3.15+
- **Frontend**: HTML5 | CSS3 | JavaScript | Bootstrap 5
- **База даних**: SQLite (розробка) | PostgreSQL (продакшн)
- **Авторизація**: django-allauth (Google, GitHub OAuth)
- **API**: drf-spectacular (OpenAPI/Swagger)
- **Тестування**: pytest | coverage.py
- **CI/CD**: GitHub Actions

##  Встановлення та запуск


### 1️⃣ Клонування репозиторію

```bash
git clone https://github.com/SMatvii/LifeManager.git
cd finassistant
```

### 2️⃣ Створення віртуального середовища

**Windows:**
```bash
# Створення віртуального середовища
python -m venv venv

# Активація
venv\Scripts\activate

```
**Linux/Mac:**
```bash
# Створення віртуального середовища
python3 -m venv venv

# Активація
source venv/bin/activate
```

### 3️⃣ Встановлення залежностей

```bash
# Оновлення pip до останньої версії
python -m pip install --upgrade pip

# Встановлення всіх залежностей з requirements.txt
pip install -r requirements.txt
```

### 4️⃣ Налаштування середовища

```bash
# Перехід до директорії Django проекту
cd finassistant

# Копіювання файлу налаштувань (або створення власного)
copy .env.example .env    # Windows
# або
cp .env.example .env      # Linux/Mac
```

**Відредагуйте файл `.env`:**
```env
SECRET_KEY="your-super-secret-key-here"
DEBUG="True"
DATABASE_NAME="db.sqlite3"

# Опціонально: для соціальної авторизації
GOOGLE_CLIENT_ID="your-google-client-id"
GOOGLE_CLIENT_SECRET="your-google-client-secret"
GITHUB_CLIENT_ID="your-github-client-id"
GITHUB_CLIENT_SECRET="your-github-client-secret"
```

### 5️⃣ Міграції бази даних

```bash
# Створення міграцій для моделей
python manage.py makemigrations

# Застосування міграцій
python manage.py migrate

# Перевірка статусу міграцій
python manage.py showmigrations

# Опціонально: створення суперкористувача для адмінки
python manage.py createsuperuser
```

### 6️⃣ Запуск сервера розробки

```bash
# Запуск Django сервера
python manage.py runserver

# Сервер буде доступний за адресою:
# http://127.0.0.1:8000/
```

## Тестування

### Запуск тестів

```bash
# Всі тести
python manage.py test

# Тести з pytest
pytest

# Тести з покриттям коду
pytest --cov=core --cov-report=html --cov-report=term-missing

# Тести конкретного додатку
python manage.py test core
```

## API Документація

Після запуску сервера доступні:

- **Swagger UI**: http://127.0.0.1:8000/api/schema/swagger-ui/
- **ReDoc**: http://127.0.0.1:8000/api/schema/redoc/
- **JSON Schema**: http://127.0.0.1:8000/api/schema/
- **Django Admin**: http://127.0.0.1:8000/admin/

### Основні ендпоінти API

```
GET    /api/transactions/     - Список транзакцій
POST   /api/transactions/     - Створення транзакції
GET    /api/transactions/{id}/ - Деталі транзакції
PUT    /api/transactions/{id}/ - Оновлення транзакції
DELETE /api/transactions/{id}/ - Видалення транзакції

GET    /api/categories/       - Список категорій
POST   /api/categories/       - Створення категорії

GET    /api/events/           - Список подій
POST   /api/events/           - Створення події

GET    /api/profile/          - Профіль користувача
```

## Основні команди Django

```bash
# Створення нового додатку
python manage.py startapp myapp

# Створення міграцій після змін в моделях
python manage.py makemigrations

# Застосування міграцій
python manage.py migrate

# Створення суперкористувача
python manage.py createsuperuser

# Запуск інтерактивної оболонки Django
python manage.py shell
```

## Внесок у проект

1. **Fork** репозиторію
2. Створіть **feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit** ваші зміні: `git commit -m 'Add some AmazingFeature'`
4. **Push** в branch: `git push origin feature/AmazingFeature`
5. Відкрийте **Pull Request**

Цей проект ліцензовано під [MIT License](LICENSE) - див. файл LICENSE для деталей.