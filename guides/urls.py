from django.urls import path
from .views import (
    GuideCreateView,
    GuideDetailView,
    GuideListView,
    HeroListView,

)

app_name = 'guides'

urlpatterns = [
    path('create/', GuideCreateView.as_view(), name='create'),
    path('<int:pk>/', GuideDetailView.as_view(), name='details'),
    path('heroes/', HeroListView.as_view(), name='heroes'),
    path('', GuideListView.as_view(), name='all'),

]
