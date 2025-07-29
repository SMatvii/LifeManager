from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from drf_spectacular.utils import extend_schema, OpenApiExample
from .models import User, Category, Transaction, Event
from .serializers import UserSerializer, CategorySerializer, TransactionSerializer, EventSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user).order_by('name')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @extend_schema(
        summary="Отримати категорії за типом",
        description="Повертає категорії доходів або витрат",
        responses={200: CategorySerializer(many=True)}
    )
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        category_type = request.query_params.get('type', 'expense')
        categories = self.get_queryset().filter(type=category_type)
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).select_related('category', 'user').order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        summary="Статистика транзакцій",
        description="Повертає загальну суму доходів та витрат",
        responses={200: {
            "type": "object", 
            "properties": {
                "total_income": {"type": "number"},
                "total_expense": {"type": "number"},
                "balance": {"type": "number"}
            }
        }}
    )
    @action(detail=False, methods=['get'])
    def stats(self, request):
        transactions = self.get_queryset()
        
        income = transactions.filter(category__type='income').aggregate(
            total=Sum('amount'))['total'] or 0
        expense = transactions.filter(category__type='expense').aggregate(
            total=Sum('amount'))['total'] or 0
        
        return Response({
            'total_income': income,
            'total_expense': expense,
            'balance': income - expense
        })

    @extend_schema(
        summary="Транзакції за типом",
        description="Повертає транзакції доходів або витрат",
        responses={200: TransactionSerializer(many=True)}
    )
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        transaction_type = request.query_params.get('type', 'expense')
        transactions = self.get_queryset().filter(category__type=transaction_type)
        serializer = self.get_serializer(transactions, many=True)
        return Response(serializer.data)


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user).select_related('category', 'user').order_by('date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        summary="Завершити подію",
        description="Позначити подію як завершену",
        responses={200: EventSerializer}
    )
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        event = self.get_object()
        event.completed = True
        event.save()
        serializer = self.get_serializer(event)
        return Response(serializer.data)

    @extend_schema(
        summary="Активні події",
        description="Повертає незавершені події",
        responses={200: EventSerializer(many=True)}
    )
    @action(detail=False, methods=['get'])
    def active(self, request):
        events = self.get_queryset().filter(completed=False)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    @extend_schema(
        summary="Мій профіль",
        description="Повертає дані поточного користувача",
        responses={200: UserSerializer}
    )
    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
