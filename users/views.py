from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.template import loader


def index(request):
    template = loader.get_template('users/templates/index.html')
    context = {}
    return render(request, 'users/templates/index.html', context)

def get_post(request, post_id):
    return HttpResponse('Вы читаете статью %s', post_id)
