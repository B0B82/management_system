from rest_framework import generics
from event.serializers import EventDetailSerializer, EventListSerializer
from event.models import Event


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventDetailSerializer


class EventListView(generics.ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all()


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
