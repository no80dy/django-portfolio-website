from django.shortcuts import render

from .models import Post, Tag


def home(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()

    context = {
        'title': 'Home',
        'posts': posts,
        'tags': tags,
    }

    return render(request, 'base/home.html', context)


def posts(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()

    context = {
        'title': 'Home',
        'posts': posts,
        'tags': tags,
    }
    return render(request, 'base/posts.html', context)


def post(request):
    context = {
        'title': 'Posts',
    }
    return render(request, 'base/post.html', context)


def portfolio(request):
    context = {
        'title': 'Portfolio',
    }
    return render(request, 'base/portfolio.html', context)
