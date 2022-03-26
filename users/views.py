from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
from django.template import loader
from django.views import generic

from users.models import Post

class IndexView(generic.ListView):
    template_name = 'users/templates/index.html'
    model = Post

class DetailView(generic.DetailView):
    template_name = 'users/templates/detail.html'
    model = Post

def insert(request):
    if request.method == 'GET':
        return render(request, 'users/templates/insert.html')
    else:
        post=Post(title=request.POST['title'], body=request.POST['body'],
                  author=request.POST['author'], dttm_add=datetime.now())
        post.save()
        return render(request, 'users/templates/insert.html')

class InsertView(generic.CreateView):
    model = Post
    template_name = 'users/templates/insert2.html'
    fields = ['title', 'author', 'body']


# def index(request):
#     template = loader.get_template('users/templates/index.html')
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request, 'users/templates/index.html', context)

# def get_post(request, post_id):
#     return HttpResponse('Вы читаете статью %s', post_id)
