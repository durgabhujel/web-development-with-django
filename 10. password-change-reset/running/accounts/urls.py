from django.urls import path
from .views import SignUpView, password_changeview, password_resetview
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/', password_changeview.as_view(), name='password_change'),
    path('password_reset/', password_resetview.as_view(), name='password_reset'),

]
