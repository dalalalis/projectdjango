
from django import forms
from .models import EventItem

class EventItemForm(forms.ModelForm):
    class Meta:
        model=EventItem
        fields=["name", "numberofseats", "image", "dateofevent",]
        widgets={"dateofevent": forms.SelectDateWidget()}

        
        

