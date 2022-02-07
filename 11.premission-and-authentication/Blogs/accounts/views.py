from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# def change_password(request):
#     return render(request, 'registration/password_change_form.html')

# def reset_password(request):
#     return render(request, 'registration/reset_password.html')
