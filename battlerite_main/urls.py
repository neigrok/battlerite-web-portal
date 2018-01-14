from django.urls import path
from .views import HomeTemplateView

app_name = 'battlerite_main'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),

]
