from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
    posts = Post.objects.order_by("date_added")
    context = {"posts": posts}
    return render(request, 'chirper/index.html',  context)


@login_required
def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid:
            new_post = form.save(commit=False)
            new_post.poster = request.user
            form.save()
            return redirect('chirper:index')
    
    context = {'form': form}
    return render(request, 'chirper/new_post.html', context)


@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.poster != request.user:
        raise Http404
    else:
        if request.method != 'POST':
            form = PostForm(instance=post)
        else:
            form = PostForm(instance=post, data=request.POST)
            if form.is_valid:
                form.save()
                return redirect('chirper:index')
    context = {'post': post, 'form':form}
    return render(request, 'chirper/edit_post.html', context)


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post' : post}
    if post.poster == request.user:
        if request.method != 'POST':
            return render(request, 'chirper/edit_post.html', context)
        else: 
            post.delete()   
            return redirect('chirper:index')
    else:
        raise Http404