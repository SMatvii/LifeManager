# LifeManager - Фінансовий помічник

<div align="center">
  <img src="finassistant/core/static/img/favicon.ico" alt="LifeManager Logo" width="64" height="64">
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
git clone https://github.com/SMatvii/finassistant.git
cd finassistant

# Встановлення залежностей
pip install -r requirements.txt
```

### Крок 2: Налаштування бази даних
```bash
# Міграції
python manage.py migrate

# Створення суперкористувача
python manage.py createsuperuser

```
### Крок 3: OAuth налаштування (опціонально)
```bash
# Запуск сервера
python manage.py runserver

# Відкрийте http://localhost:8000/admin/
# Додайте Social Application для Google та GitHub
```

### Крок 4: Користування
- Відкрийте **http://localhost:8000**
- Зареєструйтесь або увійдіть
- Почніть керувати своїми фінансами!

### Крок 5: Тестування
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
- `tests/test_integration.py` - інтеграційні тести
- `tests/conftest.py` - конфігурація pytest та фікстури

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
├── 📁 tests/
│   ├── conftest.py
│   ├── test_models.py
│   ├── test_views.py
│   ├── test_forms.py
│   └── test_integration.py
│   ├── admin.py             # Адмін панель
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

## Технології

- **Backend**: Django 4.2+, Python 3.12+
- **Frontend**: Bootstrap 5.3, Custom CSS, Chart.js
- **База даних**: SQLite (розробка), PostgreSQL (продакшн)
- **Авторизація**: django-allauth (OAuth2)
- **Іконки**: Bootstrap Icons, SVG іконки

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

## Скріншоти

*Додайте скріншоти вашого проекту тут*

---

## Внесок

Ласкаво просимо робити внесок! Будь ласка:

1. Зробіть Fork проекту
2. Створіть Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit зміни (`git commit -m 'Add some AmazingFeature'`)
4. Push до Branch (`git push origin feature/AmazingFeature`)
5. Відкрийте Pull Request
---