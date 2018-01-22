from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Guide, Hero

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


# Create your views here.
class GuideListView(ListView):
    model = Guide

    def get_context_data(self, **kwargs):
        page = self.request.GET.get('page', 1)
        paginator = Paginator(Guide.objects.all(), 15)

        context = super().get_context_data(**kwargs)
        context['guide_list'] = paginator.get_page(page)

        return context


class GuideDetailView(DetailView):
    model = Guide


class GuideCreateView(LoginRequiredMixin, CreateView):
    model = Guide
    login_url = reverse_lazy('users:login')
    fields = ['owner', 'name', 'desc', 'cards']


class GuideLike(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None, *args, **kwargs):
        user = request.user
        guide = Guide.objects.filter(pk=pk).first()
        data = {"likes": None}

        if guide is not None:
            if user in guide.likes.all():
                guide.likes.remove(user)
            else:
                guide.likes.add(user)
            data["likes"] = len(guide.likes.all())
        return Response(data)


class HeroListView(ListView):
    model = Hero

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['melee_heroes'] = self.model.objects.filter(role='m')
        context['ranged_heroes'] = self.model.objects.filter(role='r')
        context['support_heroes'] = self.model.objects.filter(role='s')

        return context


class HeroDetailView(DetailView):
    model = Hero


