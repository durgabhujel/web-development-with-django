from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class password_changeview(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('Password_change_done')
    template_name = 'registration/password_change.html'


class password_resetview(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('password_reset_done')
    template_name = 'registration/password_reset_form.html'
