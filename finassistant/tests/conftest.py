import os
import pytest
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finassistant.settings')
django.setup()

pytestmark = pytest.mark.django_db

@pytest.fixture(scope='session')
def django_db_setup():
    from django.conf import settings
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'ATOMIC_REQUESTS': True,
    }

@pytest.fixture
def user_factory():
    from django.contrib.auth import get_user_model
    User = get_user_model()
    def create_user(username='testuser', email='test@example.com', password='testpass123'):
        return User.objects.create_user(username=username, email=email, password=password)
    return create_user

@pytest.fixture
def category_factory():
    from core.models import Category
    def create_category(name='Тестова категорія', cat_type='expense', owner=None):
        return Category.objects.create(name=name, type=cat_type, owner=owner)
    return create_category

@pytest.fixture
def transaction_factory():
    from core.models import Transaction
    def create_transaction(user, category=None, amount='100.00', description='Тест'):
        return Transaction.objects.create(
            user=user, category=category, 
            amount=Decimal(str(amount)), description=description
        )
    return create_transaction

@pytest.fixture
def event_factory():
    from core.models import Event
    from datetime import date, timedelta
    def create_event(user, title='Тестова подія', amount='100.00', category=None, priority='medium', days_ahead=1):
        return Event.objects.create(
            user=user, 
            title=title, 
            amount=Decimal(str(amount)),
            category=category,
            priority=priority,
            date=date.today() + timedelta(days=days_ahead)
        )
    return create_event

@pytest.fixture
def authenticated_client(user_factory):
    from django.test import Client
    user = user_factory()
    client = Client()
    client.login(username='testuser', password='testpass123')
    client.user = user
    return client

@pytest.fixture
def user():
    from django.contrib.auth import get_user_model
    User = get_user_model()
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )

@pytest.fixture
def category():
    from core.models import Category
    return Category.objects.create(
        name='Test Category',
        type='expense'
    )

@pytest.fixture
def transaction(user, category):
    from core.models import Transaction
    return Transaction.objects.create(
        user=user,
        category=category,
        amount=100.00,
        description='Test transaction',
        type='expense'
    )
