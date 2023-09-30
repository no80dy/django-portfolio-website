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
    context = {
        'title': 'Posts',
    }

    posts = Post.objects.all()
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
