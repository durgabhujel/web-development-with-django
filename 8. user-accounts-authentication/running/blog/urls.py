from django.urls import path
from .views import blogs,  blog_detail ,BlogCreateView,BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('blogs/', blogs, name='blogs'),
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'), #new
    path('blogs/blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/<int:pk>/edit/',BlogUpdateView.as_view(), name='blog_edit'),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),#new
]
