from django.urls import path
from .views import blogs,  blog_detail

urlpatterns = [
    path('blogs/', blogs, name='blogs'),
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'), #new
]
