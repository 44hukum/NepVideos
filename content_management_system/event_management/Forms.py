from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets

from .models import Booking,Competition_Registration


class CreatorBooking(forms.ModelForm):
    """
    Responsible for handlng Event Booking form
    """
    class Meta:
        model = Booking
        fields = [
            'name','email','phonenumber'
        ]
        widgets ={
            'name': forms.TextInput(attrs={
                'placeholder':'Name',
                'class':'form-control',
                'style':"margin-top: 0px"
            }),
            'email': forms.TextInput(attrs={
               'placeholder':'Email',
               'class':'form-control',
               'style':"margin-top: 12px"
            }),
            'phonenumber':forms.TextInput(attrs={
                'placeholder':'phonenumber',
                'class':'form-control',
                'style':"margin-top: 12px"
            }) 
        }

class Competition_Registration(forms.ModelForm):
    """
    Responsible for handlng Competition Booking form
    """
    class Meta:
        model = Competition_Registration
        fields = [
            'name','email','phonenumber'
        ]
        widgets ={
            'name': forms.TextInput(attrs={
                'placeholder':'Competitor Name',
                'class':'form-control',
                'style':"margin-top: 0px"
            }),
            'email': forms.TextInput(attrs={
               'placeholder':'Competitor Email',
               'class':'form-control',
               'style':"margin-top: 12px"
            }),
            'phonenumber':forms.TextInput(attrs={
                'placeholder':'Competitor phonenumber',
                'class':'form-control',
                'style':"margin-top: 12px"
            }) 
        }


# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
