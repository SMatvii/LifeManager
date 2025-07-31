import pytest
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from core.models import Category, Transaction, Event
from core.serializers import (
    CategorySerializer, 
    TransactionSerializer, 
    EventSerializer,
    UserSerializer
)

User = get_user_model()


@pytest.mark.django_db
class TestCategorySerializer:
    
    def setup_method(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_category_serializer_valid_data(self):
        """Тест серіалізації категорії з валідними даними"""
        data = {
            'name': 'Test Category',
            'type': 'expense'
        }
        serializer = CategorySerializer(data=data)
        assert serializer.is_valid()
        
    def test_category_serializer_invalid_type(self):
        """Тест серіалізації категорії з невалідним типом"""
        data = {
            'name': 'Test Category',
            'type': 'invalid_type'
        }
        serializer = CategorySerializer(data=data)
        assert not serializer.is_valid()

    def test_category_serializer_validation_error(self):
        """Тест валідації назви категорії"""
        data = {
            'name': '',  # Порожнє ім'я
            'type': 'expense'
        }
        serializer = CategorySerializer(data=data)
        assert not serializer.is_valid()
        assert 'name' in serializer.errors


@pytest.mark.django_db
class TestEventSerializer:
    
    def setup_method(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(
            name='Test Category',
            type='expense',
            owner=self.user
        )

    def test_event_serializer_valid_priority(self):
        """Тест валідації пріоритету події - валідне значення"""
        data = {
            'user': self.user.id,
            'title': 'Test Event',
            'amount': '100.00',
            'category': self.category.id,
            'priority': 'high',
            'date': '2025-12-31'
        }
        serializer = EventSerializer(data=data)
        assert serializer.is_valid()

    def test_event_serializer_invalid_priority(self):
        """Тест валідації пріоритету події - невалідне значення"""
        data = {
            'user': self.user.id,
            'title': 'Test Event',
            'amount': '100.00',
            'category': self.category.id,
            'priority': 'invalid_priority',
            'date': '2025-12-31'
        }
        serializer = EventSerializer(data=data)
        assert not serializer.is_valid()
        assert 'priority' in serializer.errors

    def test_event_priority_validation_message(self):
        """Тест повідомлення про помилку валідації пріоритету"""
        serializer = EventSerializer()
        with pytest.raises(ValidationError) as exc_info:
            serializer.validate_priority('wrong_priority')
        
        assert "Priority must be 'low', 'medium', or 'high'" in str(exc_info.value)

    def test_event_serializer_read_only_fields(self):
        """Тест що category_name та user_username є read-only"""
        event = Event.objects.create(
            user=self.user,
            title='Test Event',
            amount=200.00,
            category=self.category,
            priority='medium',
            date='2025-12-31'
        )
        
        serializer = EventSerializer(event)
        data = serializer.data
        
        assert 'category_name' in data
        assert 'user_username' in data
        assert data['category_name'] == self.category.name
        assert data['user_username'] == self.user.username


@pytest.mark.django_db  
class TestTransactionSerializer:
    
    def setup_method(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(
            name='Test Category',
            type='expense',
            owner=self.user
        )

    def test_transaction_serializer_valid_data(self):
        """Тест серіалізації транзакції з валідними даними"""
        data = {
            'user': self.user.id,
            'category': self.category.id,
            'amount': '150.75',
            'description': 'Test transaction'
        }
        serializer = TransactionSerializer(data=data)
        assert serializer.is_valid()

    def test_transaction_serializer_read_only_fields(self):
        """Тест read-only полів транзакції"""
        transaction = Transaction.objects.create(
            user=self.user,
            category=self.category,
            amount=100.50,
            description='Test transaction'
        )
        
        serializer = TransactionSerializer(transaction)
        data = serializer.data
        
        assert 'category_name' in data
        assert 'user_username' in data
        assert data['category_name'] == self.category.name
        assert data['user_username'] == self.user.username


@pytest.mark.django_db
class TestUserSerializer:
    
    def test_user_serializer_fields(self):
        """Тест полів користувача в серіалізаторі"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        
        serializer = UserSerializer(user)
        data = serializer.data
        
        expected_fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        for field in expected_fields:
            assert field in data

    def test_user_serializer_read_only_fields(self):
        """Тест read-only полів користувача"""
        serializer = UserSerializer()
        read_only_fields = serializer.Meta.read_only_fields
        
        assert 'id' in read_only_fields
        assert 'date_joined' in read_only_fields
