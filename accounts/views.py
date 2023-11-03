# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Add validation here as needed.
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('login')  # Replace 'home' with the URL name for your home page
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('poll_list')  # Replace 'home' with the URL name for your home page
        else:
            # Handle invalid login
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'accounts/home.html')