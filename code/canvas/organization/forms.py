from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from authentication_user.models import User
from events.models import Event,Images

genres =(
    ("1", "Photography"),
    ("2", "Abstract Art"),
    ("3", "Handicraft"),
    
)
  

class CreateUserForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "p-2 mt-8 rounded-xl",
        "type": "text",
        "placeholder": "Username"
    }))

    
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "p-2 mt-1 rounded-xl",
        "type": "email",
        "placeholder": "Email"
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "p-2 mt-1 rounded-xl",
        "type": "password",
        "placeholder": "Password"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "p-2 mt-1 rounded-xl",
        "type": "password",
        "placeholder": "Confirm Password"
    }))

    

    class Meta:
        model = User
        fields = ['email','username', 'password1', 'password2']


