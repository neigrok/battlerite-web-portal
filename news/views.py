from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import News
# Create your views here.


class NewsTemplateView(TemplateView):

    template_name = "news.html"

    def get_context_data(self, **kwargs):
        page = self.request.GET.get('page', 1)
        paginator = Paginator(News.objects.all(), 5)

        context = super().get_context_data(**kwargs)
        context['news_list'] = paginator.get_page(page)
        return context


class NewsDetailView(DetailView):
    model = News
