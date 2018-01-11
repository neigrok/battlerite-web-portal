from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import News
# Create your views here.


class NewsTemplateView(TemplateView):

    template_name = "news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.objects.all()[:5]
        return context


class NewsDetailView(DetailView):
    model = News