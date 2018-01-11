from django.db import models
from battlerite import settings

HERO_ROLES = (('m', 'Melee'),
              ('r', 'Range'),
              ('s', 'Support'),

              )


class Hero(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=HERO_ROLES)
    lore = models.TextField()
    cut_lore = models.CharField(max_length=200)
    portrait = models.ImageField(upload_to=settings.MEDIA_ROOT)
    #ablities

    def __str__(self):
        return self.name
