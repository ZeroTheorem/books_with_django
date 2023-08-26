from django import forms
from .models import UserProfile, CastomUser


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = CastomUser
        fields = ["username", "first_name", "email"]

    def clean_password_2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password_2"]:
            raise forms.ValidationError("Password don't match")
        else:
            return cd["password_2"]

    def clean_email(self):
        data = self.cleaned_data["email"]
        if CastomUser.objects.filter(email=data).exists():
            raise forms.ValidationError("Email alredy in use")
        return data


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar", "date_of_birth"]
