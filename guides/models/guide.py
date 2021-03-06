from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from .card import Card
from .hero import Hero


# Create your models here.
class Guide(models.Model):
    owner = models.ForeignKey(Hero, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='author')
    name = models.CharField(max_length=120)
    desc = models.TextField()
    cards = models.ManyToManyField(Card)
    likes = models.ManyToManyField(User, related_name='likes')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp', '-updated']

    def get_absolute_url(self):
        return reverse('guides:details', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.name} for {self.owner.name} by {self.author}"
