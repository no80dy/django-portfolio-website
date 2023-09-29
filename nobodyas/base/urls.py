from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('post/', views.post, name='post'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
]
