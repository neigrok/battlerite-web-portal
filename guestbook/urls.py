from django.urls import path
from .views import AddCommentView

app_name = 'news'

urlpatterns = [
    path('addcommment/', AddCommentView.as_view(), name='add'),

]
