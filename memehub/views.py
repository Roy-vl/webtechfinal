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
    for profiles in Profile.objects.all():
        if profiles.user == request.user:
            profile = profiles
            break
    seenmemes = profile.seenMemes.all()
    for meme in Meme.objects.all():
        if meme not in seenmemes:
            profile.seenMemes.add(meme)
            profile.save()
            return render(request, 'judge.html', { 'meme': meme })
    return render(request, 'outoffmemes.html', { 'meme': meme })
	
	
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
