import pytest
from django.core.management import call_command
from django.contrib.auth import get_user_model
from core.models import Category

User = get_user_model()


@pytest.mark.django_db
class TestCreateCategoriesCommand:
    
    def test_create_categories_command(self):
        """Тест команди створення базових категорій"""
        # Переконуємося що категорій немає
        assert Category.objects.count() == 0
        
        # Запускаємо команду
        call_command('create_categories')
        
        # Перевіряємо що категорії створені
        assert Category.objects.count() > 0
        
        # Перевіряємо що є категорії доходів та витрат
        income_categories = Category.objects.filter(type='income')
        expense_categories = Category.objects.filter(type='expense')
        
        assert income_categories.exists()
        assert expense_categories.exists()
        
        # Перевіряємо конкретні категорії
        expected_income = ['Зарплата', 'Фріланс', 'Інвестиції', 'Подарунки']
        expected_expense = ['Їжа', 'Транспорт', 'Комунальні послуги', 'Розваги', 'Покупки', 'Здоров\'я']
        
        income_names = list(income_categories.values_list('name', flat=True))
        expense_names = list(expense_categories.values_list('name', flat=True))
        
        for name in expected_income:
            assert name in income_names
            
        for name in expected_expense:
            assert name in expense_names

    def test_create_categories_command_idempotent(self):
        """Тест що команда може виконуватися кілька разів без дублювання"""
        # Запускаємо команду двічі
        call_command('create_categories')
        initial_count = Category.objects.count()
        
        call_command('create_categories')
        final_count = Category.objects.count()
        
        # Кількість не повинна змінитися
        assert initial_count == final_count
