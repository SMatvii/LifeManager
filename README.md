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

### Крок 3: Налаштування бази даних
```bash
# Міграції
python manage.py migrate

# Створення базових категорій
python manage.py create_categories

# Створення суперкористувача
python manage.py createsuperuser
```

### Крок 4: Запуск проекту
```bash
# Запуск сервера
python manage.py runserver

# Відкрийте http://localhost:8000
```

### Крок 5: API документація (Swagger)
```bash
# Swagger UI (інтерактивна): http://localhost:8000/api/docs/
# ReDoc: http://localhost:8000/api/redoc/
# JSON Schema: http://localhost:8000/api/schema/
```

### Крок 6: Тестування
```bash
# Всі тести
pytest

# З покриттям коду  
pytest --cov=core

# Конкретні тести
pytest tests/test_models.py
pytest -m "unit"
```

---

## 📁 Структура проекту

```
finassistant/
├── manage.py
├── requirements.txt
├── pytest.ini
├── finassistant/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── api_views.py
│   ├── api_urls.py
│   ├── admin.py
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── management/
│   │   └── commands/
│   │       └── create_categories.py
│   ├── serializers/
│   ├── templates/
│   └── static/
└── tests/
    ├── conftest.py
    ├── test_models.py
    ├── test_views.py
    ├── test_forms.py
    └── test_integration.py
```

---

## API Documentation

### Swagger UI
**http://localhost:8000/api/docs/** - Інтерактивна документація

### Основні API endpoints:
- **Categories**: `/api/categories/` - CRUD операції з категоріями
- **Transactions**: `/api/transactions/` - Фінансові транзакції
- **Events**: `/api/events/` - Планування подій
- **Profile**: `/api/profile/me/` - Профіль користувача

---

## Технології

- **Backend**: Django 5.2+, Python 3.12+, Django REST Framework 3.16+
- **API Documentation**: drf-spectacular (OpenAPI 3.0)
- **Frontend**: Bootstrap 5.3, Custom CSS, Chart.js
- **База даних**: SQLite (розробка), PostgreSQL (продакшн)
- **Авторизація**: django-allauth (OAuth2)
- **Іконки**: Bootstrap Icons, SVG іконки

---

## Функціонал

- **Dashboard**: Графіки доходів/витрат, останні транзакції
- **Категорії**: Їжа, Транспорт, Зарплата, Покупки  
- **Транзакції**: Додавання доходів та витрат
- **Події**: Планування майбутніх операцій з пріоритетами
- **OAuth**: Авторизація через Google та GitHub
- **API**: REST API з Swagger документацією
---

## Внесок

Ласкаво просимо робити внесок! Будь ласка:

1. Зробіть Fork проекту
2. Створіть Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit зміни (`git commit -m 'Add some AmazingFeature'`)
4. Push до Branch (`git push origin feature/AmazingFeature`)
5. Відкрийте Pull Request.
---