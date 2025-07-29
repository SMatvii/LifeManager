# LifeManager - Фінансовий помічник

<div align="center">
  <img src="finassistant/core/static/img/LifeManager.png" alt="LifeManager Logo" width="623" height="548">
</div>


**Сучасний особистий фінансовий менеджер на Django з красивим інтерфейсом та потужними можливостями**

![Django](https://img.shields.io/badge/Django-4.2+-092E20?logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## Особливості

### Авторизація
- **OAuth2 аутентифікація** через Google та GitHub
- **Класична реєстрація** з підтвердженням email
- **Сучасний дизайн** форм входу та реєстрації з градієнтами та анімаціями
- **Соціальні іконки** з фірмовими кольорами Google/GitHub

### Фінансовий менеджмент
- **Категорії**: Їжа, Транспорт, Зарплата, Покупки та інші
- **Транзакції**: Додавання доходів та витрат з детальним описом
- **Події**: Планування майбутніх фінансових операцій з пріоритетами
- **Аналітика**: Інтерактивні графіки доходів/витрат (Chart.js)

### Профіль користувача
- **Персональний профіль** з можливістю завантаження аватара
- **Персоналізована панель** з привітанням та статистикою
- **Адаптивна навігація** з Bootstrap dropdown меню

### Сучасний дизайн
- **Bootstrap 5.3** з кастомними CSS стилями
- **Градієнтні фони** та smooth анімації
- **Адаптивний дизайн** для всіх пристроїв
- **Красивий футер** з соціальними посиланнями
- **Система сповіщень** з анімованими алертами

---

## Швидкий старт

### Крок 1: Встановлення
```bash
# Клонування репозиторію
git clone https://github.com/SMatvii/LifeManager.git
cd finassistant

# Встановлення залежностей
pip install -r requirements.txt
```

### Крок 2: Налаштування середовища
Створіть файл `.env` в корені проекту та додайте наступні змінні:
```env
SECRET_KEY=""
DEBUG="True"
DATABASE_URL="sqlite:///db.sqlite3"
DATABASE_NAME="db.sqlite3"

GOOGLE_CLIENT_ID = ""
GOOGLE_CLIENT_SECRET = ""

GITHUB_CLIENT_ID = ""
GITHUB_CLIENT_SECRET = ""
```

секретний ключ можна згенерувати за допомогою Django:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```


Нижче покроково описано, як отримати ці значення.

---

## 🔐 Як отримати Google OAuth 2.0 Client ID та Secret

1. Перейдіть на [Google Cloud Console](https://console.cloud.google.com/).
2. Створіть новий проєкт або виберіть існуючий.
3. У меню зліва оберіть **APIs & Services > Credentials**.
4. Натисніть **Create Credentials > OAuth 2.0 Client ID**.
5. Якщо потрібно, спочатку налаштуйте **OAuth consent screen**:
   - Оберіть тип (Internal або External)
   - Заповніть необхідну інформацію: App name, User support email, Developer contact info.
6. Оберіть **Application type: Web application**.
7. Додайте авторизовані URI:
   - **Authorized redirect URIs**, в нашому випадку це: `http://127.0.0.1:8000/accounts/google/login/callback/`
8. Після створення ви отримаєте:
   - **Client ID**
   - **Client Secret**

Збережіть ці значення у `.env` файлі вашого проєкту.

---

## 🔐 Як отримати GitHub OAuth Client ID та Secret

1. Перейдіть на [GitHub Developer Settings](https://github.com/settings/developers).
2. Оберіть **OAuth Apps** → натисніть **New OAuth App**.
3. Заповніть форму:
   - **Application name**: назва вашого додатку
   - **Homepage URL**: в нашому випадку це, `http://127.0.0.1:8000/`
   - **Authorization callback URL**: в нашому випадку це, `http://127.0.0.1:8000/accounts/github/login/callback/`
4. Натисніть **Register Application**.
5. Ви отримаєте:
   - **Client ID**
   - Натисніть **Generate a new client secret**, щоб отримати **Client Secret**

Збережіть значення у `.env` файлі.

---

### Крок 3: Налаштування бази даних та міграції
```bash
# Перейдіть до папки проекту
cd finassistant

# Створення міграцій (якщо потрібно)
python manage.py makemigrations

# Застосування міграцій до бази даних
python manage.py migrate

# Створення суперкористувача для доступу до адмін панелі
python manage.py createsuperuser

# Перевірка міграцій (опціонально)
python manage.py showmigrations

# Перевірка статусу проекту
python manage.py check
```

### Крок 4: OAuth налаштування (опціонально)
```bash
# Запуск сервера розробки
python manage.py runserver

# Відкрийте http://localhost:8000/admin/
# Увійдіть як суперкористувач
# Перейдіть до Sites → додайте domain: 127.0.0.1:8000
# Перейдіть до Social Applications → додайте провайдерів:
#   - Provider: Google, Name: Google OAuth, Client ID: ваш_google_client_id
#   - Provider: GitHub, Name: GitHub OAuth, Client ID: ваш_github_client_id
```

### Крок 5: Користування
- Відкрийте **http://localhost:8000**
- Зареєструйтесь або увійдіть
- Почніть керувати своїми фінансами!

### Крок 6: API та Swagger документація
```bash
# Запуск сервера розробки
python manage.py runserver

# Відкрийте у браузері:
# Swagger UI (інтерактивна документація): http://localhost:8000/api/docs/
# ReDoc (альтернативна документація): http://localhost:8000/api/redoc/

# Генерація схеми у файл (опціонально)
python manage.py spectacular --color --file schema.json

# Перевірка API endpoints
curl http://localhost:8000/api/categories/
curl http://localhost:8000/api/docs/
```

#### 🎯 Особливості Swagger документації:
- **Інтерактивність**: Можна тестувати API прямо в браузері
- **Автентифікація**: Підтримка сесійної авторизації Django
- **Деталізація**: Повні описи параметрів, відповідей та помилок
- **Фільтрація**: Пошук endpoints за тегами та операціями
- **Експорт**: Можливість завантажити OpenAPI схему
- **Українська локалізація**: Описи та помилки українською мовою

### Крок 7: Тестування
```bash
# Запуск всіх тестів
pytest

# Запуск тестів з детальним виводом
pytest tests/ -v

# Запуск тестів з покриттям коду
pytest --cov=core

# Запуск конкретного тестового файлу
pytest tests/test_models.py

# Запуск без попереджень
pytest tests/ --disable-warnings
```

**Структура тестів:**
- `tests/test_models.py` - тести моделей Django
- `tests/test_views.py` - тести views та URL
- `tests/test_forms.py` - тести форм
- `tests/test_api.py` - тести API endpoints та Swagger
- `tests/test_integration.py` - інтеграційні тести
- `tests/conftest.py` - конфігурація pytest та фікстури

### Крок 8: Робота з міграціями
```bash
# Створення нових міграцій при зміні моделей
python manage.py makemigrations

# Створення міграцій для конкретного додатку
python manage.py makemigrations core

# Застосування міграцій
python manage.py migrate

# Перегляд статусу міграцій
python manage.py showmigrations

#### Корисні команди для міграцій:
- `makemigrations` - створює файли міграцій на основі змін в моделях
- `migrate` - застосовує міграції до бази даних
- `showmigrations` - показує статус усіх міграцій
- `sqlmigrate` - показує SQL код конкретної міграції
- `--fake` - позначає міграцію як застосовану без виконання

---

## 📁Структура проекту

```
finassistant/
├── 📁 finassistant/          # Основні налаштування Django
│   ├── settings.py           # Конфігурація проекту
│   ├── urls.py              # URL маршрути
│   └── wsgi.py              # WSGI конфігурація
├── 📁 core/                 # Основний додаток
│   ├── models.py            # Моделі: User, Category, Transaction, Event
│   ├── views.py             # View функції та класи
│   ├── forms.py             # Django форми
│   ├── api_views.py         # API ViewSets
│   ├── api_urls.py          # API маршрути
│   ├── 📁 serializers/      # API серіалізатори
│   │   ├── __init__.py
│   │   ├── user_serializers.py
│   │   ├── category_serializers.py
│   │   ├── transaction_serializers.py
│   │   └── event_serializers.py
│   ├── 📁 migrations/       # Міграції бази даних
│   │   ├── __init__.py
│   │   └── 0001_initial.py  # Початкова міграція
│   ├── admin.py             # Адмін панель
├── 📁 tests/                # Тестування
│   ├── conftest.py          # Конфігурація pytest та фікстури
│   ├── test_models.py       # Тести моделей Django
│   ├── test_views.py        # Тести views та URL
│   ├── test_forms.py        # Тести форм
│   ├── test_api.py          # Тести API endpoints
│   └── test_integration.py  # Інтеграційні тести
├── manage.py                # Django менеджер
│   ├── 📁 templates/        # HTML шаблони
│   │   ├── base.html        # Базовий шаблон з навігацією
│   │   ├── dashboard.html   # Головна панель
│   │   ├── profile.html     # Профіль користувача
│   │   ├── 📁 account/      # Шаблони авторизації
│   │   └── 📁 socialaccount/ # OAuth шаблони
│   └── 📁 static/          # Статичні файли
│       ├── 📁 css/         # CSS стилі
│       └── 📁 img/         # Зображення
├── manage.py               # Django менеджер
├── requirements.txt        # Python залежності
└── README.md              # Документація
```

---

## API та Swagger документація

### Швидкий доступ до документації:
- **Swagger UI**: http://localhost:8000/api/docs/ - Інтерактивна документація з можливістю тестування
- **ReDoc**: http://localhost:8000/api/redoc/ - Красива читабельна документація  

### 🔧 Налаштування Swagger:
```python
# settings.py конфігурація
SPECTACULAR_SETTINGS = {
    'TITLE': 'LifeManager API',
    'DESCRIPTION': 'API для фінансового помічника LifeManager',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SCHEMA_PATH_PREFIX': '/api/',
}
```

### Використання API з автентифікацією:
1. **Увійдіть в систему**: http://localhost:8000/api-auth/login/
2. **Відкрийте Swagger**: http://localhost:8000/api/docs/
3. **Тестуйте endpoints** прямо в браузері
4. **Переглядайте відповіді** в реальному часі

### Основні API endpoints:

#### **Categories API**
```bash
GET    /api/categories/          # Список категорій
POST   /api/categories/          # Створення категорії
GET    /api/categories/{id}/     # Деталі категорії
PUT    /api/categories/{id}/     # Оновлення категорії
DELETE /api/categories/{id}/     # Видалення категорії
GET    /api/categories/by_type/  # Категорії за типом (?type=income/expense)
```

#### **Transactions API**
```bash
GET    /api/transactions/          # Список транзакцій
POST   /api/transactions/          # Створення транзакції
GET    /api/transactions/{id}/     # Деталі транзакції
PUT    /api/transactions/{id}/     # Оновлення транзакції
DELETE /api/transactions/{id}/     # Видалення транзакції
GET    /api/transactions/stats/    # Статистика (доходи/витрати/баланс)
GET    /api/transactions/by_type/  # Транзакції за типом
```

#### **Events API**
```bash
GET    /api/events/           # Список подій
POST   /api/events/           # Створення події
GET    /api/events/{id}/      # Деталі події
PUT    /api/events/{id}/      # Оновлення події
DELETE /api/events/{id}/      # Видалення події
POST   /api/events/{id}/complete/  # Завершити подію
GET    /api/events/active/    # Активні події
```

#### **Profile API**
```bash
GET    /api/profile/me/       # Мій профіль
```

### Приклади використання API:


### Авторизація API:
- **Методи автентифікації**: Сесійна автентифікація Django + Basic Auth
- **Доступ до API**: Потрібна авторизація для всіх endpoints
- **Вхід через API**: `/api-auth/login/` - форма входу Django
- **Тестування**: Використовуйте Swagger UI для інтерактивного тестування

### Додаткові команди для API:
```bash
# Перевірка API маршрутів
python manage.py show_urls | grep api

# Генерація OpenAPI схеми
python manage.py spectacular --color --file schema.json

# Валідація API
python manage.py check

# Тестування API
pytest tests/test_api.py -v
```
---

## Технології

- **Backend**: Django 5.2+, Python 3.12+, Django REST Framework 3.16+
- **API Documentation**: drf-spectacular (OpenAPI 3.0)
- **Frontend**: Bootstrap 5.3, Custom CSS, Chart.js
- **База даних**: SQLite (розробка), PostgreSQL (продакшн)
- **Авторизація**: django-allauth (OAuth2)
---

## Функціонал

### Dashboard (Панель керування)
- Інтерактивні графіки доходів/витрат
- Останні транзакції та події
- Персоналізовані привітання
- Швидкі дії

### Категорії
-**Їжа** - ресторани, продукти, доставка
-**Транспорт** - паливо, громадський транспорт, таксі
-**Зарплата** - основний дохід, бонуси
-**Покупки** - одяг, електроніка, побутові товари
-**Інше** - різні витрати та доходи

### Події (Планування)
-Планування майбутніх операцій
-Пріоритети: низький, середній, високий
-Відстеження виконання
-Нагадування
---

## Внесок

Ласкаво просимо робити внесок! Будь ласка:

1. Зробіть Fork проекту
2. Створіть Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit зміни (`git commit -m 'Add some AmazingFeature'`)
4. Push до Branch (`git push origin feature/AmazingFeature`)
5. Відкрийте Pull Request.
---
