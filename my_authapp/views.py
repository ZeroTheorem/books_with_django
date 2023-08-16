from django.shortcuts import render
from .forms import UserRegistrationForm
# Create your views here.


def registration(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'my_authapp/registration_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()

    return render(request, 'my_authapp/registration_form.html', {'user_form': form})
