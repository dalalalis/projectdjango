
from email.policy import default
from multiprocessing import Event
from pickle import TRUE
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class EventItem(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    numberofseats=models.PositiveIntegerField(validators=[
            MaxValueValidator(400) ])
    dateofevent=models.DateTimeField()   
    def __str__(self):
        return self.name 

class Booking(models.Model):
    book = models.ForeignKey("Booking", on_delete=models.CASCADE ,default=None)  # to test the booking 
    event =models.OneToOneField(EventItem, on_delete=models.CASCADE, primary_key=TRUE) #1 booking for each user
    seatbooked=models.IntegerField()

    def ___str__(self):
        return self.seatbooked 



