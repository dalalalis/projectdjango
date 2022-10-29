from multiprocessing import context
from django.shortcuts import render, redirect
from users.forms import User_register, User_edit, User_login
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from organisers.models import Booking, EventItem 

User=get_user_model()

def register_user(request):
    form=User_register()
    if request.method == "POST":
        form=User_register(request.POST)
        if form.is_valid():
            user=form.save(commit=False)

            user.set_password(user.password)  # error with access 
            user.save()

            login(request, user)
            if user.is_staff:
                return redirect("event-item-list")
            else:
                return redirect("event-item-list")
    context ={"form":form,}
    return render(request, "register.html", context)

def login_user(request):
    form =User_login()
    if request.method == "POST":
        form = User_login(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password=form.cleaned_data["password"]

            auth_user= authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                if auth_user.is_staff:
                    return redirect("event-item-list")
                else:
                    return redirect("event-item-list")
                    
    context ={"form":form,}
    return render(request, "login.html", context)
#here i think we should have to add the <is staff> to diffrentiate between user and organizer
#if staff we redirect them to the dashbourd temp in organizers

def logout_user(request):
    logout(request)
    return redirect("event-item-list")

def edit_profile(request, user_id):
    user=User.objects.get(id=user_id)
    form=User_edit(instance=user)
    print("user_id")
    # if request.user.id == user_id:
    if request.method == "POST":
        form=User_edit(request.POST, instance=user)
        print("from 2nd if")
        if form.is_valid():
            form.save()
        return redirect("event-item-list")
    context= {"form":form,
    "user":{"id":user_id}}
    return render (request, "profile.html", context) 


def booking(request,seats):
    event_booking = Booking.objects(seats)
    list = []
    booking_list = Booking.objects.filter(seats)
    for book in booking_list:
        if book in booking_list:
            list.append(True)
            return all(list)
        else:
            list.append(False)
        return all(list)
    context = {"event_booking":event_booking, "seats": "seats", }
    return render (request, "booking.html", context)

def booking_details(request):
    details = Booking.objects()
    context = {
        "details":{
            "number_of_seats": "number of seats",
            "date_of_event": "date of the event",
        }
    }
    return render (request,"booking_details.html",context)



'''
def fully_booked(request):
    form = Booking()
    if seats is valid()
        seats.set_seatsavailable(seats.seatsavailable)
        seats.save()
        return render(seatsavailable)
    elseif seats is full:
        print("Sorry, there are no available seats for this event. ") 
    
    context = {"seats": seats}
    return render (request, "booking.html", context)
    # check for count 
    '''
#used to redirect user to login page (book button in home page)
#from django.shortcuts import redirect
#def some_view(request):
    #if request.user.is_anonymous:
        #return redirect("login")


# Create your views here
