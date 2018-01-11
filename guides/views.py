from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Guide


# Create your views here.
class GuideListView(ListView):
    model = Guide

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for guide in context['object_list']:
            guide.card_imgs = guide.cards.all()

        return context


class GuideDetailView(DetailView):
    model = Guide


class GuideCreateView(CreateView):
    model = Guide
    fields = ['owner', 'name', 'desc', 'cards']
