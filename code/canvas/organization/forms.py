from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from authentication_user.models import User
from events.models import Event,Image

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


class EventForm(forms.ModelForm):

    event_name = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "placeholder": "Name"
    }))
    event_description = forms.CharField(max_length=200)
    start_date = forms.DateField() 
    start_time= forms.TimeField()
    end_date= forms.DateField() 
    end_time= forms.TimeField() 
    is_paid= forms.BooleanField(required=False, label="It is a paid event")

    fee = forms.IntegerField(widget=forms.NumberInput(attrs={
        "type": "number",
        "placeholder": "fee"
    })) 

    genre= forms.ChoiceField(choices= genres)

    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'start_date','start_time','end_date', 'end_time','is_paid','fee','genre']


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['image']
#         widgets = {
#             'image': ClearableFileInput(attrs={'multiple': True}),
#         }    