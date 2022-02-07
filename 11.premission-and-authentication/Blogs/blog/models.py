from django.db import models
from django.urls import reverse #new
from config import settings
User = settings.AUTH_USER_MODEL


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='User')  #update the author
    body = models.TextField()
    # description = models.TextField()
    header_image = models.ImageField(null=True,blank=True,upload_to='images/')
    subtitle = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('blog_detail', args=[str(self.id)])