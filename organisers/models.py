
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
    dateofevent=models.DateTimeField() # max_length is added because CharFields doesn't accept empty attribute  


    def __str__(self):
        return self.name 

class Booking(models.Model):
    event =models.OneToOneField(EventItem, on_delete=models.CASCADE, primary_key=TRUE)
    seatbooked=models.IntegerField(default=1)

    def ___str__(self):
        return self.seatbooked 



