from django.views.generic.edit import CreateView
from .models import Comment


# Create your views here.
class AddCommentView(CreateView):
    model = Comment
    fields = ['author', 'text']
    success_url = '/'
