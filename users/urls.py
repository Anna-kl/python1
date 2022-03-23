from django.contrib import admin
from django.urls import path, include

from users.views import IndexView, DetailView

urlpatterns = [
    # path('', index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>', DetailView.as_view(), name='detail')
]