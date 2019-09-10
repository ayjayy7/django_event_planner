from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView)
from events.models import Event, BookEvent

from .serializers import (EventSerializer, OrganizerSerializer, UserSerializer, UserCreateSerializer, UpdateEventSerializer, 
    EventAttendantsSerializer, AttendSerializer,UserListSerializer, AttendantsSerializer, OrganizerEventSerializer)

from .permissions import IsOrganizer, IsAttendant
from datetime import datetime



class UpcomingList(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(date__gte=datetime.today())


class OrganizerList(ListAPIView):
    serializer_class = OrganizerEventSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Event.objects.filter(organizer_id=self.kwargs['organizer_id'])


class UserList(ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated, IsAttendant]

    def get_queryset(self):
        return BookEvent.objects.filter(user=self.request.user)



class BookingEvent(CreateAPIView):
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, event_id=self.kwargs['event_id'])


class CreateEvent(CreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOrganizer]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class ModifyEvent(RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = UpdateEventSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'
    permission_classes = [IsAuthenticated, IsOrganizer]


class AttendantsView(ListAPIView):
    serializer_class = AttendSerializer
    permission_classes = [IsAuthenticated, IsOrganizer]
    def get_queryset(self):
        event = Event.objects.get(id=self.kwargs['event_id'])
        return event.bookings.all()


class Register(CreateAPIView):
    serializer_class = UserCreateSerializer
