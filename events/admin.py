from django.contrib import admin

from .models import Event,BookEvent,Profile

admin.site.register(Event)
admin.site.register(BookEvent)
admin.site.register(Profile)