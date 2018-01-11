from django.db import models
from django.urls import reverse

from .card import Card
from .hero import Hero


# Create your models here.
class Guide(models.Model):
    owner = models.ForeignKey(Hero, on_delete=models.CASCADE)
    #author
    name = models.CharField(max_length=120)
    desc = models.TextField()
    cards = models.ManyToManyField(Card)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('guides:details', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.name} for {self.owner.name} by #"
