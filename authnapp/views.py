from django.contrib import auth, messages
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from authnapp.forms import Login_form, Registration_form
# Create your views here.


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("copleated_book"))


def login_page(request):
    login_form = Login_form(data=request.POST or None)
    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("copleated_book"))
        else:
            messages.error(request, 'username or password not correct')

    content = {"login_form": login_form}
    return render(request, "authn.html", content)



def registration_page(request):

    if request.method == "POST":
        register_form = Registration_form(request.POST)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("copleated_book"))
    else:
        register_form = Registration_form()

    content = {"register_form": register_form}
    return render(request, "registration.html", content)
