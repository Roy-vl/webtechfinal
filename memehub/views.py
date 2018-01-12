from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.utils import timezone
from .models import Meme, Profile, Like
from .forms import MemeForm, ProfileForm
from django.db import transaction

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

@login_required
@transaction.atomic
def update_profile(request, pk):
    user1 = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile_form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'memehub/profile.html', {'profile_form': profile_form, 'user1': user1})

@login_required(login_url='register/login/')
def judge(request):
    #find the profile belonging to the current user
    for profiles in Profile.objects.all():
        if profiles.user == request.user:
            profile = profiles
            break
    #get the memes the user has seen
    seenmemes = profile.seenMemes.all()
    #go through all memes until one is not in the seen list
    for meme in Meme.objects.all():
        if meme not in seenmemes:
            return render(request, 'memehub/judge.html', { 'meme': meme })
    #if there is no new one go to the outofmemes page
    return render(request, 'memehub/outoffmemes.html', { 'meme': meme })

@login_required(login_url='index')
def like(request, pk):
    #find the profile belonging to the current user
    for profiles in Profile.objects.all():
        if profiles.user == request.user:
            profile = profiles
            break
    #get the memes the user has seen
    meme = get_object_or_404(Meme, pk=pk)
    profile.seenMemes.add(meme)
    profile.save()
    #add one to the like factor
    like = Like.objects.get(profile=profile, category=meme.categories)
    count = like.amount
    count += 1
    like.amount = count
    like.save()
    #set the new most liked cat if the new one is higher
    if count > Like.objects.get(profile=profile, category=profile.top_cat).amount:
        profile.top_cat = like.category
        profile.save()
    #go through all memes until one is not in the seen list
    seenmemes = profile.seenMemes.all()
    for meme in Meme.objects.all():
        if meme not in seenmemes:
            #if a new one is found open it
            return redirect('judge')
    #if there is no new one go to the outofmemes page
    return render(request, 'memehub/outoffmemes.html', { 'meme': meme })


@login_required(login_url='index')
def meh(request, pk):
    #find the profile belonging to the current user
    for profiles in Profile.objects.all():
        if profiles.user == request.user:
            profile = profiles
            break
    #get the memes the user has seen
    meme = get_object_or_404(Meme, pk=pk)
    profile.seenMemes.add(meme)
    profile.save()
    #go through all memes until one is not in the seen list
    seenmemes = profile.seenMemes.all()
    for meme in Meme.objects.all():
        if meme not in seenmemes:
            #if a new one is found open it
            return redirect('judge')
    #if there is no new one go to the outofmemes page
    return render(request, 'memehub/outoffmemes.html', { 'meme': meme })


@login_required(login_url='index')
def dislike(request, pk):
    #find the profile belonging to the current user
    for profiles in Profile.objects.all():
        if profiles.user == request.user:
            profile = profiles
            break
    #get the memes the user has seen
    meme = get_object_or_404(Meme, pk=pk)
    profile.seenMemes.add(meme)
    profile.save()
    #substract three from the like factor
    like = Like.objects.get(profile=profile, category=meme.categories)
    count = like.amount
    count -= 3
    like.amount = count
    like.save()
    #set the new most liked cat if the disliked was the current best
    if like is Like.objects.get(profile=profile, category=profile.top_cat):
        for likes in Like.objects.get(profile=profile):
            if likes.amount > count:
                profile.top_cat = likes.category
                profile.save()
    #go through all memes until one is not in the seen list
    seenmemes = profile.seenMemes.all()
    for meme in Meme.objects.all():
        if meme not in seenmemes:
            #if a new one is found open it
            return redirect('judge')
    #if there is no new one go to the outofmemes page
    return render(request, 'memehub/outoffmemes.html', { 'meme': meme })


@login_required(login_url='index')
def matches(request):
    potentials = []
    #find the profile belonging to the current user
    for profiles in Profile.objects.all():
        if profiles.user == request.user:
            profile = profiles
            break
    for potmatch in Profile.objects.all():
        if potmatch.top_cat is profile.top_cat:
            potentials.append(potmatch)
        if potentials is 5:
            return render(request, 'memehub/matches.html', { 'matches': potentials })
    if potentials is 0:
        return render(request, 'memehub/nomatches.html')
    return render(request, 'memehub/matches.html', { 'matches': potentials })
