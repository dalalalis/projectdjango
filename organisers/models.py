from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class EventItem(models.Model):
    name=models.CharField(max_length=30)
    image=models.TextField()
    #using the method she taught us yesterday
    organiser=models.TextField()
    #im guessing this is the foreign key 
    numberofseats=models.PositiveIntegerField(validators=[
            MaxValueValidator(400), ])

    dateofevent=models.CharField(max_length=12)
    #input_formats=["%d/%m/%Y %H:%M"]
    #bookedseats=

    def __str__(self):
        return self.name

    

