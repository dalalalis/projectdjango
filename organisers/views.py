
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from organisers import models
from .forms import EventItemForm
from .models import EventItem

# Create your views here.
def get_event_items(request: HttpRequest) -> HttpResponse:
    event_items: list[models.EventItem] = list(models.EventItem.objects.all())
    context = {
        "event_items": event_items,
    }
    return render(request, "event_item_list.html", context)

def create_event_item (request):
    form= EventItemForm()
    if request.method == "POST":
        form=EventItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("event-item-list")
    context={"form":form }
    return render (request, "create_event_item.html", context )

def update_store_item (request,item_id ):
    store_item=EventItem.objects.get(id= item_id)
    form= EventItemForm(instance=event_item)
    context= {"form":form,
    "event_item":{"id":event_item.id}}
    if request.method == "POST":
        form=EventItemForm(request.POST, instance=event_item)
        if form.is_valid():
            form.save()
            return redirect("event-item-list")
    return render (request, "update_event_item.html", context)

def delete_event_item (request, item_id):
    event_item=EventItem.objects.get(id=item_id).delete()
    return redirect("event-item-list")




