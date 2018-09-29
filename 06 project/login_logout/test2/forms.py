from django import forms
from django.contrib.auth.forms import UserCreationForm

#here we are extending user creation form to add email field, which gives by user models

from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=20)



    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

#we have class Meta, where we tell Django
# which model should be used to create this form (model = User).