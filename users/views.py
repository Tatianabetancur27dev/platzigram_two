from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("hola")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    else:
        return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')

