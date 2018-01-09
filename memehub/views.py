from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Meme
from django.shortcuts import redirect


def index(request):
    return render(request, 'memehub/index.html')


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('memehub/index.html' )
    else:
        form = PostForm()
    return render(request, 'memehub/post_edit.html', {'form': form})


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
