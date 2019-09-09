from django.contrib import admin

from .models import Event,BookEvent

admin.site.register(Event)
admin.site.register(BookEvent)