from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    posts = Post.objects.order_by("date_added")
    context = {"posts": posts}
    return render(request, 'chirper/index.html',  context)

def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('chirper:index')
    
    context = {'form': form}
    return render(request, 'chirper/new_post.html', context)


def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('chirper:index')
    context = {'post': post, 'form':form}
    return render(request, 'chirper/edit_post.html', context)
        
