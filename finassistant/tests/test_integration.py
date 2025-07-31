import pytest
from decimal import Decimal
from django.test import Client
from django.urls import reverse
from core.models import User, Category, Transaction, Event


@pytest.mark.django_db
class TestDataIntegrity:

    def test_user_deletion_cascade(self, user_factory, category_factory, transaction_factory, event_factory):
        user = user_factory()
        category = category_factory(name='Тест', cat_type='expense', owner=user)
        transaction = transaction_factory(user=user, category=category, amount='100.00')
        event = event_factory(user=user, title='Тестова подія')
        
        user_id = user.id
        user.delete()
        
        assert Category.objects.filter(owner_id=user_id).count() == 0
        assert Transaction.objects.filter(user_id=user_id).count() == 0
        assert Event.objects.filter(user_id=user_id).count() == 0


@pytest.mark.django_db
class TestWorkflow:
    
    def test_complete_transaction_workflow(self, authenticated_client):
        form_data = {
            'category_choice': 'Їжа',
            'amount': '150.50',
            'description': 'Обід'
        }
        
        response = authenticated_client.post(reverse('add_transaction', kwargs={'type': 'expense'}), data=form_data)
        assert response.status_code == 302
        
        transaction = Transaction.objects.filter(user=authenticated_client.user).first()
        assert transaction.amount == Decimal('150.50')
        
        response = authenticated_client.get(reverse('dashboard'))
        assert response.status_code == 200


@pytest.mark.django_db
class TestAPIBasic:
    """Базові тести API для покращення покриття"""
    
    def test_api_categories_list(self, authenticated_client, category_factory):
        """Тест отримання списку категорій через API"""
        user = authenticated_client.user
        category_factory(name='Test Category', cat_type='expense', owner=user)
        
        response = authenticated_client.get('/api/categories/')
        assert response.status_code == 200
        
    def test_api_transactions_list(self, authenticated_client):
        """Тест отримання списку транзакцій через API"""
        response = authenticated_client.get('/api/transactions/')
        assert response.status_code == 200
        
    def test_api_profile(self, authenticated_client):
        """Тест отримання профілю через API"""
        response = authenticated_client.get('/api/profile/me/')
        assert response.status_code == 200