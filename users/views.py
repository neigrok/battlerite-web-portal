from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = '/'
    # Ignore requests from authenticated users
