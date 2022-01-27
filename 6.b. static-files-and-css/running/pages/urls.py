from django.urls import path
from .views import HomePageView,ContactPageView,AboutPageView,skillPageView

urlpatterns = [
    #path('home/', HomePageView.as_view(), name='home'),
    path('', HomePageView.as_view(), name='home'),
   path('contact/', ContactPageView.as_view(), name='contact'),
   path('about/', AboutPageView.as_view(), name='about'),
   path('skill/', skillPageView.as_view(), name='skill'),
]
