from django.db import models
# from django.urls import reverse 

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='User')
    body = models.TextField()
    header_image = models.ImageField(null=True,blank=True,upload_to='images/')
    subtitle = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.title

    # def get_absolute_url(self): 
    #     return reverse('blog_detail', args=[str(self.id)])