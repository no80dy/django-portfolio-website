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


def post(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'base/post.html', {'post': post})


def portfolio(request):
    context = {
        'title': 'Portfolio',
    }
    return render(request, 'base/portfolio.html', context)


def contacts(request):
    return render(request, 'base/contacts.html')


def about(request):
    return render(request, 'base/about.html')
