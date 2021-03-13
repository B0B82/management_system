from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class EventType(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    info = models.JSONField(help_text='Value must be valid JSON')
    timestamp = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} created by {self.user}"
