from django.db import models
from battlerite import settings
from .hero import Hero

CARD_KINDS = (('con', 'Control'),
              ('mix', 'Mixed'),
              ('mob', 'Mobility'),
              ('off', 'Offense'),
              ('sur', 'Survival'),

              )


class Card(models.Model):
    owner = models.ForeignKey(Hero, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=240)
    kind = models.CharField(max_length=3, choices=CARD_KINDS)
    picture = models.ImageField(upload_to=settings.MEDIA_ROOT)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner.name} : {self.name}"
