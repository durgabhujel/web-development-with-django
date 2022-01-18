from django.urls import path
from .views import *

urlpatterns = [
        path('home/', homePageView, name='home'),
        path('about/', aboutPageView, name='about'),
        path('contact/', contactPageView, name='contact'),
        path('project/', projectView, name='project'),
]
