from django.urls import path
from .views import (
    GuideCreateView,
    GuideDetailView,
    GuideListView,
    HeroListView,
    GuideLike,

)

app_name = 'guides'

urlpatterns = [
    path('create/', GuideCreateView.as_view(), name='create'),
    path('<int:pk>/', GuideDetailView.as_view(), name='details'),
    path('<int:pk>/like/', GuideLike.as_view(), name='like'),
    path('heroes/', HeroListView.as_view(), name='heroes'),
    path('', GuideListView.as_view(), name='all'),

]
