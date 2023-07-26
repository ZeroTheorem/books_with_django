from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import my_User

class Login_form(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(Login_form, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autocomplete'] = "off"

    class Meta:
        model = my_User
        fields = ('username', 'password')


class Registration_form(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(Registration_form, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs['autocomplete'] = "off"
            field.help_text = ""


    class Meta:
        model = my_User
        fields = ('username', 'password1', 'password2')
