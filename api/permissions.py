from rest_framework.permissions import BasePermission




class IsOrganizer(BasePermission):
	message = "You must be the organizer of this event"

	def has_object_permission(self, request, view, obj):
		if request.user == obj.organizer:
			return True
		else:
			return False


class IsAttendant(BasePermission):
	message = "You must be the attendant of this event"

	def has_object_permission(self, request, view, obj):
		if request.user == obj.user:
			return True
		else:
			return False
