from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import UserProfile
from .serializers import UserProfileSerializer

# Render registration template
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse


def register_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Hash the password before saving
            password = form.cleaned_data['password']
            form.cleaned_data['password'] = make_password(password)

            # Save the user data
            form.save()
            return HttpResponse("User registered successfully!")  # You can change this to a redirect to a success page
        else:
            return render(request, 'register.html', {'form': form, 'error': 'Form is invalid'})
    else:
        form = UserProfileForm()

    return render(request, 'register.html', {'form': form})


# Render login template
def login_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return render(request, 'login.html', {'error': 'Username or password missing'})

        user = authenticate(username=username, password=password)
        if user is not None:
            return render(request, 'login.html', {'message': 'Login successful'})
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
