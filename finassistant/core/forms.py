from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Transaction, Category, Event

User = get_user_model()

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Назва категорії (наприклад: Кафе, Бензин, Подарунки)'
            }),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name.strip()) < 2:
            raise ValidationError('Назва категорії повинна містити мінімум 2 символи')
        return name.strip()


class TransactionForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('', 'Оберіть категорію'),
        ('expense', [
            ('Їжа', 'Їжа'),
            ('Транспорт', 'Транспорт'),
            ('Покупки', 'Покупки'),
            ('Розваги', 'Розваги'),
            ('Комунальні', 'Комунальні послуги'),
            ('Здоров\'я', 'Здоров\'я'),
            ('Одяг', 'Одяг'),
            ('Інше_витрати', 'Інше'),
        ]),
        ('income', [
            ('Зарплата', 'Зарплата'),
            ('Фріланс', 'Фріланс'),
            ('Бонус', 'Бонус'),
            ('Подарунки', 'Подарунки'),
            ('Інше_доходи', 'Інше'),
        ]),
    ]
    
    category_choice = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control mb-2',
            'id': 'category-select'
        }),
        label='Швидкий вибір категорії'
    )
    
    new_category = forms.CharField(
        max_length=50, 
        required=False, 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Або введіть свою категорію'
        }),
        label='Власна категорія'
    )
    
    class Meta:
        model = Transaction
        fields = ['amount', 'category', 'description']
        widgets = {
            'amount': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Сума',
                'step': '0.01',
                'min': '0'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Опис транзакції'
            }),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        self.transaction_type = kwargs.pop('transaction_type', None)
        super().__init__(*args, **kwargs)
        
        if user and self.transaction_type:
            self.fields['category'].queryset = Category.objects.filter(
                type=self.transaction_type, 
                owner__in=[user, None]
            )
            filtered_choices = [('', 'Оберіть категорію')]
            for group_name, choices in self.CATEGORY_CHOICES:
                if group_name == self.transaction_type:
                    filtered_choices.extend(choices)
            self.fields['category_choice'].choices = filtered_choices
        elif user:
            self.fields['category'].queryset = Category.objects.filter(owner__in=[user, None])
            
        self.fields['category'].required = False
        self.fields['category'].empty_label = "Або оберіть існуючу"

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise ValidationError('Сума повинна бути більшою за 0')
        if amount > 999999.99:
            raise ValidationError('Сума занадто велика')
        return amount

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        category_choice = cleaned_data.get('category_choice')
        new_category = cleaned_data.get('new_category')
        
        if not category and not category_choice and not new_category:
            raise ValidationError('Оберіть існуючу категорію або створіть нову')
        
        return cleaned_data


class EventForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('', 'Оберіть категорію'),
        ('Їжа', 'Їжа'),
        ('Транспорт', 'Транспорт'),
        ('Покупки', 'Покупки'),
        ('Розваги', 'Розваги'),
        ('Зарплата', 'Зарплата'),
        ('Фріланс', 'Фріланс'),
        ('Подарунки', 'Подарунки'),
        ('Інше', 'Інше'),
    ]
    
    category_choice = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control mb-2'
        }),
        label='Швидкий вибір категорії'
    )
    
    new_category = forms.CharField(
        max_length=50, 
        required=False, 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Або введіть свою категорію'
        }),
        label='Власна категорія'
    )
    
    class Meta:
        model = Event
        fields = ['title', 'description', 'amount', 'category', 'priority', 'date']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Назва події'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Опис події'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Сума (необов\'язково)',
                'step': '0.01',
                'min': '0'
            }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
            self.fields['category'].queryset = Category.objects.filter(owner__in=[user, None])
            self.fields['category'].required = False
            self.fields['category'].empty_label = "Або оберіть існуючу"

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title.strip()) < 3:
            raise ValidationError('Назва події повинна містити мінімум 3 символи')
        return title.strip()

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount <= 0:
            raise ValidationError('Сума повинна бути більшою за 0')
        return amount

    def clean_date(self):
        date = self.cleaned_data['date']
        from django.utils import timezone
        if date < timezone.now().date():
            raise ValidationError('Дата події не може бути в минулому')
        return date


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть новий нікнейм'
        }),
        help_text='Унікальний нікнейм (тільки букви, цифри та @/./+/-/_ символи)'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly'
        }),
        help_text='Email не може бути змінений'
    )
    
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Розкажіть про себе...'
        })
    )
    
    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'bio', 'avatar', 'phone', 'birth_date']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '+380...',
                'pattern': r'^\+?[\d\s\-\(\)]+$'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and not self.instance.can_change_username:
            self.fields['username'].widget.attrs['readonly'] = True
            self.fields['username'].help_text = 'Нікнейм не може бути змінений для цього типу акаунту'

    def clean_username(self):
        username = self.cleaned_data['username']
        
        if self.instance and not self.instance.can_change_username:
            return self.instance.username
        
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise ValidationError('Користувач з таким нікнеймом вже існує.')
        
        if len(username.strip()) < 3:
            raise ValidationError('Нікнейм повинен містити мінімум 3 символи')
        
        return username.strip()

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            import re
            if not re.match(r'^\+?[\d\s\-\(\)]+$', phone):
                raise ValidationError('Невірний формат телефону')
        return phone

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date:
            from django.utils import timezone
            from datetime import date
            
            if birth_date > timezone.now().date():
                raise ValidationError('Дата народження не може бути в майбутньому')
            
            age = (timezone.now().date() - birth_date).days // 365
            if age > 120:
                raise ValidationError('Невірна дата народження')
        
        return birth_date

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if bio and len(bio) > 500:
            raise ValidationError('Біографія не може перевищувати 500 символів')
        return bio