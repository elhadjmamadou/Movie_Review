from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ('username', 'email', "avatar" )