from django.db import models
from django.urls import reverse #new

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)  #ForeignKey allows many-to-one relationships between models , this means a author can have many blog posts
    body = models.TextField()
    subtitle = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.title
