from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Guide, Hero


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


class GuideCreateView(LoginRequiredMixin, CreateView):
    model = Guide
    login_url = reverse_lazy('users:login')
    fields = ['owner', 'name', 'desc', 'cards']


class HeroListView(ListView):
    model = Hero

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['melee_heroes'] = self.model.objects.filter(role='m')
        context['ranged_heroes'] = self.model.objects.filter(role='r')
        context['support_heroes'] = self.model.objects.filter(role='s')

        return context


