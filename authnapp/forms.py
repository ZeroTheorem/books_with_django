from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import my_User

class Login_form(AuthenticationForm):

    class Meta:
        model = my_User
        fields = ('username', 'password')


class Registration_form(UserCreationForm):

    class Meta:
        model = my_User
        fields = ('username', 'password')
