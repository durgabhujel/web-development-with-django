from unittest.util import _MAX_LENGTH
from django.db import models

class homepage(models.Model):
    title=models.CharField(max_length=50)
    p1=models.TextField()
    p2=models.TextField()
    header_image = models.ImageField(null=True,blank=True,upload_to='images/')
    skills1=models.TextField(max_length=100)
    skill2=models.TextField(max_length=20)
    tools=models.TextField(max_length=30)
    header_image2=models.ImageField(null=True,blank=True,upload_to='image/')

    #def __str__(self):
       # return self.body_title





