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
    if request.user.is_authenticated is True:
        return redirect('judge')
    else:
        return redirect('login')
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
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'memehub/profile.html', {
        'profile_form': profile_form
    })

@login_required
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

@login_required
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
    try:
        like = Like.objects.get(profile=profile, category=meme.categories)
        likability = like.amount
    except Like.DoesNotExist:
        Like.objects.create(profile=profile, category=meme.categories, amount = 0)
        likability = 1
    like = Like.objects.get(profile=profile, category=meme.categories)
    count = like.amount
    count += 1
    like.amount = count
    like.save()
    #set the new most liked cat if the new one is higher
    try:
        likability = Like.objects.get(profile=profile, category=profile.top_cat).amount
    except Like.DoesNotExist:
        likability = 0
    if count > likability:
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


@login_required
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


@login_required
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
    try:
        like = Like.objects.get(profile=profile, category=meme.categories)
        likability = like.amount
    except Like.DoesNotExist:
        Like.objects.create(profile=profile, category=meme.categories, amount = 0)
        likability = 1
    like = Like.objects.get(profile=profile, category=meme.categories)
    count = like.amount
    count -= 3
    like.amount = count
    like.save()
    #set the new most liked cat if the disliked was the current best
    try:
        best = Like.objects.get(profile=profile, category=profile.top_cat)
    except Like.DoesNotExist:
        best = Like.objects.create(profile=profile, category=profile.top_cat, amount = 0)
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


@login_required
def matches(request):
    potentials = []
    #find the profile belonging to the current user
    for profiles in Profile.objects.all():
        if profiles.user == request.user:
            profile = profiles
            break
    pcat = profile.top_cat
    for potmatch in Profile.objects.all():
        potcat = potmatch.top_cat
        if pcat == potcat and potmatch != profile:
            potentials.append(potmatch)
    if not potentials:
        return render(request, 'memehub/nomatches.html')
    return render(request, 'memehub/matches.html', { 'matches': potentials })

