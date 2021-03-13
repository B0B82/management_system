from django.contrib import admin
from . import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('user', 'event_type', 'info', 'timestamp', 'created_at')
    list_filter = ('event_type', 'timestamp')


admin.site.register(models.EventType)
