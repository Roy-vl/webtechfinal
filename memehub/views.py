from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Meme, Profile
from django.shortcuts import redirect
from .forms import MemeForm 

def index(request):
    return render(request, 'memehub/index.html')

def new_meme(request):
    if request.method == "POST":
        form = MemeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('newmeme')
    else:
        form = MemeForm()
    return render(request, 'memehub/new_meme.html', {'form': form})

def judge(request):
    profile = get_object_or_404(Profile, pk=1)
    for meme in Meme.objects.all():
        for profiles in Profile.objects.all():
            if profiles.user == request.user:
                profile = profiles
        seenmemes = profile.seenMemes.all()
        for seenId in seenmemes:
            if meme.id != seenId.pk:
                Profile.seenMemes.append(meme.id)
                Profile.save()
                return render(request, 'judge.html', { 'meme': meme })
        return render(request, 'judge.html', { 'meme': meme })
	
	
def post_remove(request, pk):
    post = get_object_or_404(Meme, pk=pk)
    post.delete()
    return redirect('post_list')

def post_edit(request, pk):
    post = get_object_or_404(Meme, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('base.html' )
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
