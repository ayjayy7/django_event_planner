from django.db import models

from django.contrib.auth.models import User

class Event(models.Model):
    organizer = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    location = models.CharField(max_length=120)
    date = models.DateField()
    time = models.TimeField()
    seats = models.IntegerField()

    def __str__(self):
        return self.title

