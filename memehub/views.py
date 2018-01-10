
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Meme, Profile
from .forms import MemeForm 

# Create your views here.
def index(request):
    return render(request, 'memehub/index.html')

def login(request):
    return render(request, 'registration/login.html')

def logout(request):
    return render(request, 'registration/logged_out.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            person = auth_authenticate(username=username, password=raw_password)
            auth_login(request, person)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required(login_url='register/login/')
def judge(request):
    for profiles in Profile.objects.all():
        if profiles.user == request.user:
            profile = profiles
            break
    seenmemes = profile.seenMemes.all()
    for meme in Meme.objects.all():
        if meme not in seenmemes:
            profile.seenMemes.add(meme)
            profile.save()
            return render(request, 'memehub/judge.html', { 'meme': meme })
    return render(request, 'memehub/outoffmemes.html', { 'meme': meme })

        
