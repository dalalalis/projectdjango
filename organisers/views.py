
from multiprocessing import Event
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from organisers import models
from .forms import EventItemForm
from .models import EventItem
import datetime
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your views here.

def get_event_items(request: HttpRequest) -> HttpResponse:  
      event_items: list[models.EventItem] = list[models.EventItem.objects.all()]    
      context = {"event_items": event_items,}    
      return render(request, "event_item_list.html", context)

'''
def get_event_items(request.user):
    if request.user.is_staff:
        events=EventItem.objects.filter(id=user.id)
        _events=[]
        for event in events:
            if event.date >datetime.now():
                return _events.append(
                    {"id": event.id, 
                    "name": event.name,
                    "image": event.image,
                    "dateofevent": event.dateofevent,
                    "numberofseats": event.numberofseats,
                    } )
            else: 
                return 
    else:
        events=Event.object.all()
        _events=[]
        return _events.append()

    context = {"events": _events}
    return render (request, "event_item_list.html", context)   
  '''               



                

def create_event_item(request):
    form= EventItemForm()
    if request.method == "POST":
        print("here")
        form=EventItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("event-item-list")
    context={"form":form }
    return render (request, "create_event_item.html", context )

def update_event_item (request,item_id ):
    event_item=EventItem.objects.get(id= item_id)
    form= EventItemForm(instance=event_item)
    context= {"form":form,
    "event_item":{"id":event_item.id}}
    if request.method == "POST":
        form=EventItemForm(request.POST, instance=event_item )
        if form.is_valid():
            form.save()
            return redirect("event-item-list")
    return render (request, "update_event_item.html", context)

def delete_event_item (request, item_id):
    event_item=EventItem.objects.get(id=item_id).delete()
    return redirect("event-item-list")




