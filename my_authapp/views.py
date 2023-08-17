from django.shortcuts import render
from .forms import UserRegistrationForm, ProfileEditForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            return render(
                request, "my_authapp/registration_done.html", {"new_user": new_user}
            )
    else:
        form = UserRegistrationForm()

    return render(request, "my_authapp/registration_form.html", {"user_form": form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = ProfileEditForm(instance=request.user.profile)

    return render(request, "my_authapp/edit.html", {"user_form": user_form})
