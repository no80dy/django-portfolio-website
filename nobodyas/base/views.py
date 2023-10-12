from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import PostForm
from .filters import PostFilter


def home(request):
    context = {
        'title': 'Home',
    }

    return render(request, 'base/home.html', context)


def posts(request):
    posts = Post.objects.filter(is_active=True)
    post_filter = PostFilter(request.GET, queryset=posts)
    posts = post_filter.qs

    page_number = request.GET.get('page')
    paginator = Paginator(posts, 6)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'title': 'Posts',
        'posts': posts,
        'post_filter': post_filter,
        'paginator': paginator,
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


@login_required(login_url='home')
def delete_post(request, id):
    post = Post.objects.get(pk=id)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')

    context = {'item': post}

    return render(request, 'base/delete.html', context)
