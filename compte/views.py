from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from compte.forms import RegistrationForm


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('membre_view')
            else:
                return render(request, 'registration/login.html', {})
        else:
            return render(request, 'registration/login.html', {})
    else:
        return redirect('membre_view')


def logout_view(request):
    logout(request)
    return redirect('login_view')


def register_view(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login_view')
        else:
            return render(request, 'registration/register.html', {'user_form': user_form})
    else:
        user_form = RegistrationForm()
        return render(request, 'registration/register.html', {'user_form':user_form})

