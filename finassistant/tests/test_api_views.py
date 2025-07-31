import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Category, Transaction, Event

User = get_user_model()


@pytest.mark.django_db
class TestCategoryAPIViewSet:
    
    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(
            name='Test Category',
            type='expense',
            owner=self.user
        )

    def test_list_categories(self):
        url = reverse('category-list')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1

    def test_create_category(self):
        url = reverse('category-list')
        data = {
            'name': 'New Category',
            'type': 'income'
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Category.objects.filter(name='New Category').exists()

    def test_get_category_detail(self):
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == 'Test Category'

    def test_update_category(self):
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        data = {
            'name': 'Updated Category',
            'type': 'expense'
        }
        response = self.client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        self.category.refresh_from_db()
        assert self.category.name == 'Updated Category'

    def test_delete_category(self):
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Category.objects.filter(pk=self.category.pk).exists()

    def test_categories_by_type(self):
        Category.objects.create(name='Income Cat', type='income', owner=self.user)
        
        url = reverse('category-by-type')
        response = self.client.get(url, {'type': 'income'})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['type'] == 'income'

    def test_unauthenticated_access_denied(self):
        self.client.force_authenticate(user=None)
        url = reverse('category-list')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
class TestTransactionAPIViewSet:
    
    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(
            name='Test Category',
            type='expense',
            owner=self.user
        )
        self.transaction = Transaction.objects.create(
            user=self.user,
            category=self.category,
            amount=100.50,
            description='Test transaction'
        )

    def test_list_transactions(self):
        url = reverse('transaction-list')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1

    def test_create_transaction(self):
        url = reverse('transaction-list')
        data = {
            'category': self.category.id,
            'amount': '250.75',
            'description': 'New transaction',
            'user': self.user.id
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Transaction.objects.filter(description='New transaction').exists()

    def test_transaction_stats(self):
        income_category = Category.objects.create(
            name='Income', type='income', owner=self.user
        )
        Transaction.objects.create(
            user=self.user,
            category=income_category,
            amount=500.00,
            description='Income transaction'
        )
        
        url = reverse('transaction-stats')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert 'total_income' in response.data
        assert 'total_expense' in response.data
        assert 'balance' in response.data

    def test_transactions_by_type(self):
        url = reverse('transaction-by-type')
        response = self.client.get(url, {'type': 'expense'})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1


@pytest.mark.django_db 
class TestEventAPIViewSet:
    
    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(
            name='Test Category',
            type='expense',
            owner=self.user
        )
        self.event = Event.objects.create(
            user=self.user,
            title='Test Event',
            amount=200.00,
            category=self.category,
            priority='medium',
            date='2025-12-31'
        )

    def test_list_events(self):
        url = reverse('event-list')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1

    def test_create_event(self):
        url = reverse('event-list')
        data = {
            'title': 'New Event',
            'amount': '300.00',
            'category': self.category.id,
            'priority': 'high',
            'user': self.user.id,
            'date': '2024-12-01'
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Event.objects.filter(title='New Event').exists()

    def test_complete_event(self):
        url = reverse('event-complete', kwargs={'pk': self.event.pk})
        response = self.client.post(url)
        assert response.status_code == status.HTTP_200_OK
        self.event.refresh_from_db()
        assert self.event.completed == True

    def test_active_events(self):
        """Тест отримання активних подій"""
        url = reverse('event-active')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1  # 1 активна подія


@pytest.mark.django_db
class TestUserProfileAPIViewSet:
    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        self.client.force_authenticate(user=self.user)

    def test_get_my_profile(self):
        url = reverse('profile-me')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['username'] == 'testuser'
        assert response.data['email'] == 'test@example.com'
        assert response.data['first_name'] == 'Test'
