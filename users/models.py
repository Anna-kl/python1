from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    body = models.TextField()
    dttm_add = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index', args=[])

