from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request):
    # if not request.user.is_authenticated:
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
    # else:
    #     return redirect('membre_view')


def logout_view(request):
    logout(request)
    return redirect('login_view')


def register(request):
    pass
