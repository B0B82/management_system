from rest_framework import serializers
from event.models import Event


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'user', 'event_type', 'info', 'timestamp', 'created_at')


class EventDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = '__all__'
