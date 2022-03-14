from django.contrib import admin
from django.urls import path, include

from users.views import index, get_post

urlpatterns = [
    path('', index, name='index'),
    path('<int:post_id>', get_post, name='post')
]