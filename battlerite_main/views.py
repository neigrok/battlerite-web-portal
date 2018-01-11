from django.views.generic.base import TemplateView
from news.models import News
from guestbook.models import Comment
from guestbook.forms import CommentForm

# Create your views here.
class HomeTemplateView(TemplateView):

    template_name = "main_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.objects.all()[:5]
        context['comment_list'] = Comment.objects.all()[:5]
        context['guestbook_form'] = CommentForm()

        return context
