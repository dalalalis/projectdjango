"""projectdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
#from users import views as users_views
from organisers import views as event_views 
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static 
from users.views import booking as user_booking
from users import views as booking
from users import views as booking_details


#check how to use user_views find it url in project
#check if need to import class 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("organiser/", event_views.get_event_items, name="event-item-list"),
    path("organiser/add/", event_views.create_event_item, name="create-event-item" ),
    path("organiser/edit/<int:item_id>/", event_views.update_event_item, name="update-event-item" ),
    path("organiser/delete/<int:item_id>/", event_views.delete_event_item, name="delete-event-item"),
    path("hello/", event_views.home_page, name="home" ),
    path("register/", user_views.register_user, name="register"),
    path("logout/", user_views.logout_user, name="logout"),
    path("login/", user_views.login_user, name="login"),
    path("user/<int:user_id>/",user_views.edit_profile, name="user-edit"),
    path("booking/", user_views.booking, name="booking"),
    path("details/", user_views.booking_details, name="booking-details")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
