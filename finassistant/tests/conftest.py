import os
import sys
import django
import pytest
from django.conf import settings
from django.test import Client
from django.contrib.auth import get_user_model
from decimal import Decimal
from datetime import date, timedelta

# Додаємо корінь проекту до Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

def pytest_configure(config):
    """Конфігурація pytest для Django"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finassistant.settings')
    django.setup()

# Глобальний маркер для доступу до БД
pytestmark = pytest.mark.django_db

@pytest.fixture(scope='session')
def django_db_setup():
    """Налаштування тестової бази даних"""
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'timeout': 20,
        }
    }

@pytest.fixture
def user_factory():
    """Фабрика для створення користувачів"""
    User = get_user_model()
    
    def create_user(username='testuser', email='test@example.com', password='testpass123', **kwargs):
        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
            **kwargs
        )
    return create_user

@pytest.fixture
def admin_user(user_factory):
    """Створення користувача-адміністратора"""
    return user_factory(
        username='admin',
        email='admin@example.com', 
        is_staff=True,
        is_superuser=True
    )

@pytest.fixture
def category_factory():
    """Фабрика для створення категорій"""
    from core.models import Category
    
    def create_category(name='Тестова категорія', cat_type='expense', owner=None, **kwargs):
        return Category.objects.create(
            name=name,
            type=cat_type,
            owner=owner,
            **kwargs
        )
    return create_category

@pytest.fixture
def transaction_factory():
    """Фабрика для створення транзакцій"""
    from core.models import Transaction
    
    def create_transaction(user, category=None, amount='100.00', description='Тестова транзакція', **kwargs):
        return Transaction.objects.create(
            user=user,
            category=category,
            amount=Decimal(str(amount)),
            description=description,
            **kwargs
        )
    return create_transaction

@pytest.fixture
def event_factory():
    """Фабрика для створення подій"""
    from core.models import Event
    
    def create_event(user, title='Тестова подія', priority='medium', days_ahead=1, **kwargs):
        event_date = kwargs.pop('date', date.today() + timedelta(days=days_ahead))
        return Event.objects.create(
            user=user,
            title=title,
            priority=priority,
            date=event_date,
            **kwargs
        )
    return create_event

@pytest.fixture
def authenticated_client(user_factory):
    """Клієнт з авторизованим користувачем"""
    user = user_factory()
    client = Client()
    client.login(username='testuser', password='testpass123')
    client.user = user
    return client

@pytest.fixture
def admin_client(admin_user):
    """Клієнт з авторизованим адміністратором"""
    client = Client()
    client.login(username='admin', password='testpass123')
    client.user = admin_user
    return client

@pytest.fixture
def anonymous_client():
    """Неавторизований клієнт"""
    return Client()

@pytest.fixture
def basic_categories(category_factory):
    """Базовий набір категорій"""
    return {
        'income': category_factory(name='Зарплата', cat_type='income'),
        'expense': category_factory(name='Їжа', cat_type='expense'),
        'transport': category_factory(name='Транспорт', cat_type='expense'),
        'utilities': category_factory(name='Комунальні', cat_type='expense'),
    }

@pytest.fixture
def sample_data(user_factory, category_factory, transaction_factory, event_factory):
    """Комплексний набір тестових даних"""
    user = user_factory()
    
    # Створюємо категорії
    income_category = category_factory(name='Зарплата', cat_type='income')
    expense_category = category_factory(name='Їжа', cat_type='expense')
    
    # Створюємо транзакції
    income_transaction = transaction_factory(
        user=user, 
        category=income_category, 
        amount='30000.00',
        description='Місячна зарплата'
    )
    expense_transaction = transaction_factory(
        user=user,
        category=expense_category,
        amount='5000.00', 
        description='Продукти'
    )
    
    # Створюємо подію
    event = event_factory(
        user=user,
        title='Оплата комунальних',
        priority='high'
    )
    
    return {
        'user': user,
        'categories': {
            'income': income_category,
            'expense': expense_category
        },
        'transactions': {
            'income': income_transaction,
            'expense': expense_transaction
        },
        'events': [event]
    }

@pytest.fixture
def multiple_users(user_factory):
    """Кілька користувачів для тестування ізоляції"""
    return {
        'user1': user_factory(username='user1', email='user1@example.com'),
        'user2': user_factory(username='user2', email='user2@example.com'),
        'user3': user_factory(username='user3', email='user3@example.com'),
    }

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """Автоматично надаємо доступ до БД для всіх тестів"""
    pass
