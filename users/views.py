from django.shortcuts import render, redirect
from users.forms import User_register, User_edit, User_login
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model

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

def edit_profile(request):
    print("print")
    user=User.objects.get(request.user.id)
    form=User_edit(instance=user)
    print("hellos")
    if request.method == "POST":
        form=User_edit(request.POST, instance=user)
        print("hi")
        if form.is_valid():
            form.save()
            return redirect("event-item-list")
    context= {"form":form,
    "user":{"id":user.id}}
    return render (request, "profile.html", context) 


    '''
    make booking
    '''

#used to redirect user to login page (book button in home page)
#from django.shortcuts import redirect
#def some_view(request):
    #if request.user.is_anonymous:
        #return redirect("login")


# Create your views here.
