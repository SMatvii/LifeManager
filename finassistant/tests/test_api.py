import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from core.models import Category, Transaction


@pytest.mark.django_db
class TestCategoryAPI:
    
    def test_category_list_unauthorized(self):
        client = APIClient()
        url = '/api/categories/'
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_category_list_authorized(self, authenticated_client):
        client = APIClient()
        client.force_authenticate(user=authenticated_client.user)
        url = '/api/categories/'
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_category(self, authenticated_client):
        client = APIClient()
        client.force_authenticate(user=authenticated_client.user)
        url = '/api/categories/'
        data = {
            'name': 'Тестова категорія API',
            'type': 'expense'
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == 'Тестова категорія API'


@pytest.mark.django_db
class TestTransactionAPI:
    
    def test_transaction_stats(self, authenticated_client, category_factory, transaction_factory):
        client = APIClient()
        client.force_authenticate(user=authenticated_client.user)
        income_cat = category_factory(name='Зарплата', cat_type='income')
        expense_cat = category_factory(name='Їжа', cat_type='expense')
        
        transaction_factory(user=authenticated_client.user, category=income_cat, amount='1000')
        transaction_factory(user=authenticated_client.user, category=expense_cat, amount='300')
        
        url = '/api/transactions/stats/'
        response = client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert 'total_income' in response.data
        assert 'total_expense' in response.data
        assert 'balance' in response.data


@pytest.mark.django_db 
class TestSwaggerEndpoints:
    
    def test_swagger_ui_accessible(self):
        client = APIClient()
        url = '/api/docs/'
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_redoc_accessible(self):
        client = APIClient()
        url = '/api/redoc/'
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_schema_accessible(self):
        client = APIClient()
        url = '/api/schema/'
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
