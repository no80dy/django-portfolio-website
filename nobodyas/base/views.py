from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Tag
from .forms import PostForm


def home(request):
    context = {
        'title': 'Home',
    }

    return render(request, 'base/home.html', context)


def posts(request):
    context = {
        'title': 'Posts',
    }

    posts = Post.objects.filter(is_active=True)
    tags = Tag.objects.all()

    context = {
        'title': 'Posts',
        'posts': posts,
        'tags': tags,
    }
    return render(request, 'base/posts.html', context)


def post(request, id):
    post = Post.objects.get(pk=id)
    context = {
        'title': 'Post',
        'post': post,
    }
    return render(request, 'base/post.html', context)


def portfolio(request):
    context = {
        'title': 'Portfolio',
    }
    return render(request, 'base/portfolio.html', context)


def contacts(request):
    context = {
        'title': 'Contact me',
    }
    return render(request, 'base/contacts.html', context)


def about(request):
    context = {
        'title': 'About me',
    }
    return render(request, 'base/about.html', context)


@login_required(login_url='home')
def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {
        'form': form
    }

    return render(request, 'base/post_form.html', context)


@login_required(login_url='home')
def update_post(request, id):
    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {
        'form': form
    }

    return render(request, 'base/post_form.html', context)
