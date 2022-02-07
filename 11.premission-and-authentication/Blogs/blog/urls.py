from django.urls import path
from .views import blogs,  blog_detail ,BlogCreateView,BlogUpdateView, BlogDeleteView,profile,my_blogs

urlpatterns = [
    path('', blogs, name='home'),
    path('<int:blog_id>/', blog_detail, name='blog_detail'), #new
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('<int:pk>/edit/',BlogUpdateView.as_view(), name='blog_edit'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),#new
    path('profile/', profile, name='profile'),
    path('my_blogs/', my_blogs, name='my_blogs'),

]
