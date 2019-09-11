from django.db import models
from django.contrib.auth.models import User



class Event(models.Model):
    organizer = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=120)
    description = models.TextField()
    location = models.CharField(max_length=120)
    date = models.DateField()
    time = models.TimeField()
    seats = models.IntegerField()
    logo = models.ImageField(upload_to='restaurant_logos', null=True)

    COOKING = "cooking"
    CONCERT = "concert"
    CONFERENCE="Conference"
    CHARITY="charity"
    ART="art"
    PLAY="play"
    OTHERS="others"
    CHOICES = ( (COOKING, "cooking"), (CONCERT, "concert"), (CONFERENCE,"Conference"), (CHARITY,"charity"),(ART,"art"),(PLAY,"play"),(OTHERS,"others") )
    choice = models.CharField(max_length=7, choices=CHOICES,)
    def __str__(self):
        return self.title

    def get_seats_booked(self):
    	seats= self.bookings.all()
    	total=0
    	for seat in seats:
    		total=total+ seat.book_seats
    	return total

    def get_seats_left(self):
    	return self.seats - self.get_seats_booked()
    	
    	

class BookEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booker')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    phone_number = models.CharField(max_length=120)  #CharField
    book_seats = models.PositiveIntegerField()


