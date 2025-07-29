from rest_framework import serializers
from ..models import Event


class EventSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'user', 'user_username', 'title', 'amount', 'category', 
                 'category_name', 'priority', 'date', 'completed']
        read_only_fields = ['id']

    def validate_priority(self, value):
        if value not in ['low', 'medium', 'high']:
            raise serializers.ValidationError("Priority must be 'low', 'medium', or 'high'")
        return value
