import pytest
from decimal import Decimal
from django.test import Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.models import Transaction, Event, Category

User = get_user_model()


@pytest.mark.django_db
class TestAuthentication:
    
    def test_dashboard_requires_login(self):
        client = Client()
        response = client.get(reverse('dashboard'))
        assert response.status_code == 302
        assert '/accounts/login/' in response.url


@pytest.mark.django_db
class TestDashboard:
    
    def test_dashboard_context(self, authenticated_client, transaction_factory, category_factory):
        income_cat = category_factory(name='Зарплата', cat_type='income', owner=authenticated_client.user)
        expense_cat = category_factory(name='Їжа', cat_type='expense', owner=authenticated_client.user)
        
        transaction_factory(user=authenticated_client.user, category=income_cat, amount='1000')
        transaction_factory(user=authenticated_client.user, category=expense_cat, amount='500')
        
        response = authenticated_client.get(reverse('dashboard'))
        
        assert response.status_code == 200
        context = response.context
        assert 'balance' in context
        assert 'income' in context
        assert 'expenses' in context


@pytest.mark.django_db
class TestTransactions:
    
    def test_add_transaction_post_valid(self, authenticated_client, category_factory):
        """Тест додавання транзакції з валідними даними"""
        user = authenticated_client.user
        category = category_factory(name='Test Category', cat_type='expense', owner=user)
        
        data = {
            'category': category.id,
            'amount': '150.75',
            'description': 'Test transaction'
        }
        
        response = authenticated_client.post(reverse('add_transaction', kwargs={'type': 'expense'}), data)
        assert response.status_code == 302
        assert Transaction.objects.filter(description='Test transaction').exists()

    def test_transactions_list(self, authenticated_client, transaction_factory, category_factory):
        """Тест списку транзакцій"""
        user = authenticated_client.user
        category = category_factory(name='Test Category', cat_type='expense', owner=user)
        
        transaction_factory(user=user, category=category, amount='100', description='Test transaction')
        
        response = authenticated_client.get(reverse('transactions'))
        assert response.status_code == 200


@pytest.mark.django_db
class TestEvents:
    
    def test_add_event_get(self, authenticated_client):
        """Тест GET запиту на сторінку додавання події"""
        response = authenticated_client.get(reverse('add_event'))
        assert response.status_code == 200

    def test_events_list(self, authenticated_client, event_factory, category_factory):
        """Тест списку подій"""
        user = authenticated_client.user
        category = category_factory(name='Test Category', cat_type='expense', owner=user)
        
        event_factory(user=user, title='Test Event', amount='200', category=category, priority='medium')
        
        response = authenticated_client.get(reverse('events'))
        assert response.status_code == 200


@pytest.mark.django_db
class TestProfile:
    
    def test_profile_view(self, authenticated_client):
        """Тест перегляду профілю"""
        response = authenticated_client.get(reverse('profile'))
        assert response.status_code == 200


@pytest.mark.django_db
class TestTransactions:
    
    def test_add_transaction_post_valid(self, authenticated_client):
        form_data = {
            'category_choice': 'Їжа',
            'amount': '150.50',
            'description': 'Обід'
        }
        response = authenticated_client.post(reverse('add_transaction', kwargs={'type': 'expense'}), data=form_data)
        assert response.status_code == 302
        
        transaction = Transaction.objects.filter(user=authenticated_client.user).first()
        assert transaction.amount == Decimal('150.50')