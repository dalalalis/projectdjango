from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Events(models.Models):
    name=models.CharField(max_length=30)
    image=
    #using the method she taught us yesterday
    organiser=
    #im guessing this is the foreign key 
    numberofseats=models.PositiveIntegerField(validators=[
            MaxValueValidator(350), ])

    dateofevent=models.DateTimeField(auto_now_add=True)
    #i believe this is a function 
    bookedseats=

    def __str__(self):
        return 

    

