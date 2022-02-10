from django.urls import path
from .views import BlogAPIView,BlogDetailAPIView

urlpatterns = [
    path('', BlogAPIView.as_view()),
    path('<int:pk>', BlogDetailAPIView.as_view()),
]
