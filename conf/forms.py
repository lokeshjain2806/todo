from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usermodel


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Usermodel
        fields = '__all__'

class Signupform(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Reenter Password', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email']
