from django.urls import path
from .views import NewsTemplateView, NewsDetailView

app_name = 'news'

urlpatterns = [
    path('', NewsTemplateView.as_view(), name='news'),
    path('<slug:slug>/', NewsDetailView.as_view(), name='news_details'),

]
