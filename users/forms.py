
from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()

class User_register(forms.ModelForm):
    class Meta:
        model=User
        fields=["username", "first_name", "last_name", "email", "password"]
        widgets={"password": forms.PasswordInput()}

class User_login(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True, widget=forms.PasswordInput())

class User_edit(forms.ModelForm):
    class Meta:
        model=User
        fields=[ "first_name", "last_name", "email",]
        

 