from django.contrib import admin
from django.urls import path, include

from users.views import IndexView, DetailView, insert, InsertView

urlpatterns = [
    # path('', index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>', DetailView.as_view(), name='detail'),
    path('insert', insert, name='insert'),
    path('insert2', InsertView.as_view(), name='insert2'),
]