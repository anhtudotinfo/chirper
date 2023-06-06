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

                