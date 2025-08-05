from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    social_provider = models.CharField(max_length=50, blank=True, null=True)
    can_change_username = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.username} ({self.email})"

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"


class Category(models.Model):
    TYPE_CHOICES = (
        ('income', 'Дохід'),
        ('expense', 'Витрата'),
    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        unique_together = ['name', 'type', 'owner']


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} ({self.category}) - {self.user.username}"

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = "Транзакція"
        verbose_name_plural = "Транзакції"


class Event(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')
    date = models.DateField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.date}"

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = "Подія"
        verbose_name_plural = "Події"

    @property
    def is_overdue(self):
        from django.utils import timezone
        return self.date < timezone.now().date() and not self.completed

    @property
    def priority_color(self):
        colors = {
            'low': 'success',
            'medium': 'warning', 
            'high': 'danger'
        }
        return colors.get(self.priority, 'secondary')