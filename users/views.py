from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = '/'


class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users:login')
    template_name = "users/profile.html"