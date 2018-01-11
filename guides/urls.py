from django.urls import path
from .views import (
    GuideCreateView,
    GuideDetailView,
    GuideListView,
)

app_name = 'guides'

urlpatterns = [
    path('create/', GuideCreateView.as_view(), name='create'),
    path('<int:pk>/', GuideDetailView.as_view(), name='details'),
    path('', GuideListView.as_view(), name='all'),

]
