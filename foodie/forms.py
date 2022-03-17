from dataclasses import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from foodie.models import *
from shopcart.models import *
from profileapp.models import *


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='Username')
    first_name = forms.CharField(max_length=50, help_text='First Name')
    last_name = forms.CharField(max_length=50, help_text='Last Name')
    email = forms.EmailField(max_length=50, help_text='Email')



    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']

STATE = [
    ('Abia', 'Abia'),
    ('Abuja', 'Abuja'),
    ('Edo', 'Edo'),
    ('Kano', 'Kano'),
    ('Lagos', 'Lagos'),
    ('Ogun', 'Ogun'),
    ('Ph', 'Ph'),
]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'address', 'state', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'state': forms.Select(attrs={'class':'form-control', 'placeholder':'State'}, choices=STATE),
            'image': forms.FileInput(),
        }        

class ShopCartForm(forms.ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity', 'how_spicy']