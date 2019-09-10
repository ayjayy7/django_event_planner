from rest_framework import serializers
from django.contrib.auth.models import User
from events.models import Event, BookEvent


class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		exclude = ['organizer']



class OrganizerSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_name(self, obj):
        return (obj.organizer.first_name + obj.organizer.last_name)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.save()
        return validated_data


class UpdateEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		exclude = ['organizer',]



class EventAttendantsSerializer(serializers.ModelSerializer):
        attendants = serializers.SerializerMethodField()
        class Meta:
            model = BookEvent
            fields = ['title', 'time', 'date', 'location', 'attendants']

        def get_attendants(self,obj):
            return  obj.bookings.all #booking or booker? related name for events that take event foriegn key in BookEvent model
             # AttendantsSerializer(attendant, many=True).data

class AttendSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    eventname = serializers.SerializerMethodField()
    class Meta:
        model = BookEvent
        fields = ['username', 'eventname']
    
    def get_username(self,obj):
        return obj.user.username
    def get_eventname(self,obj):
        return obj.event.title

class UserListSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()
    
    class Meta:
        model = BookEvent
        exclude = ['user', 'event']

    def get_events(self, obj):
        return (obj.event.title)



class AttendantsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = BookEvent
        fields = ['name']

    def get_name(self, obj):
        return (obj.user.first_name + obj.user.last_name)


