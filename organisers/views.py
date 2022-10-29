
from multiprocessing import Event
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from organisers import models
from .forms import EventItemForm
from .models import EventItem
import datetime
from django.contrib.auth import get_user_model
from datetime import datetime



user=get_user_model()

# Create your views here.

# def get_event_items(request: HttpRequest) -> HttpResponse:  
#     event_items: list[models.EventItem] = list[models.EventItem.objects.all()]    
#     context = {"event_items": event_items,}    
#     return render(request, "event_item_list.html", context)


def get_event_items(request):
   
    if request.user.is_staff:
        print("STAFF")
        events=EventItem.objects.filter(user=request.user).exclude(dateofevent__lte=datetime.today())
    else:
        print("NOT STAFF")
        events=EventItem.objects.all().exclude(dateofevent__lte=datetime.today())
    _events=[]
    for event in events:
        _events.append(
                {"id":event.id,
                "user": event.user , 
                "name": event.name,
                "image": event.image,
                "dateofevent": event.dateofevent,
                "numberofseats": event.numberofseats,
                } )  

    context = {"events": _events}
    print(context)
    return render (request, "event_item_list.html", context)   

def get_event(request): #<<<<<<<<<id >>>>>>
    event=EventItem.objects.get(id=event.id)
    context = {
        "event": {event:{"id": id, 
                    "name": event.name,
                    "image": event.image,
                    "dateofevent": event.dateofevent,
                    "numberofseats": event.numberofseats,
                    }}}  

    return render(request, "article_detail_page.html", context)


def create_event_item(request):
    form= EventItemForm()
    if request.method == "POST":
        print("HERE\n") # the print work
        form=EventItemForm(request.POST, request.FILES)
        print("******************\n") #it works
        if form.is_valid():
            print("HELLO\n") # it works
            form.save() # the code stops here, why?
            return redirect("event-item-list")
        else:
            print("\n HI \n") # doesn't print 
    context={"form":form }
    return render (request, "create_event_item.html", context )

def home_page(request):
    print(user.objects)
    return render (request, "hello.html")

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

def delete_event_item (request, event_id):
    event=EventItem.objects.get(id=event_id).delete()
    return redirect("event-item-list")





