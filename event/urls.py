from django.urls import path
from event.views import *

app_name = 'event'

urlpatterns = [
    path('create/', EventCreateView.as_view()),
    path('all/', EventListView.as_view()),
    path('detail/<int:pk>/', EventDetailView.as_view()),
]
