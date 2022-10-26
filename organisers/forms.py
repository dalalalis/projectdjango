from django import forms
from django import forms
from .models import EventItem

class EventItemForm(forms.ModelForm):
    class Meta:
        model=EventItem
        fields=["name", "numberofseats", "image", "organiser", "dateofevent",]

        
        

