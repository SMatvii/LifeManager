import os
import sys
import django
import pytest
from django.conf import settings

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

def pytest_configure(config):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finassistant.settings')
    django.setup()

pytestmark = pytest.mark.django_db

@pytest.fixture(scope='session')
def django_db_setup():
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
        return User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
    return create_user

@pytest.fixture
def category_factory():
    from core.models import Category
    
    def create_category(name='Тестова категорія', cat_type='expense', owner=None):
        return Category.objects.create(
            name=name,
            type=cat_type,
            owner=owner
        )
    return create_category

@pytest.fixture
def transaction_factory():
    from core.models import Transaction
    from decimal import Decimal
    
    def create_transaction(user, category=None, amount='100.00', description='Тестова транзакція'):
        return Transaction.objects.create(
            user=user,
            category=category,
            amount=Decimal(amount),
            description=description
        )
    return create_transaction

@pytest.fixture
def event_factory():
    from core.models import Event
    from datetime import date, timedelta
    
    def create_event(user, title='Тестова подія', priority='medium', days_ahead=1):
        return Event.objects.create(
            user=user,
            title=title,
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
def sample_data(user_factory, category_factory, transaction_factory, event_factory):
    user = user_factory()
    
    income_category = category_factory(name='Зарплата', cat_type='income')
    expense_category = category_factory(name='Їжа', cat_type='expense')
    
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
