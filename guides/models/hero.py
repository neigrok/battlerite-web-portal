from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
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
    slug = models.SlugField(unique=True, blank=True)
    #ablities

    def __str__(self):
        return self.name


def toppings_changed(sender, instance, **kwargs):
        instance.slug = slugify(instance.name, allow_unicode=True)


pre_save.connect(toppings_changed, sender=Hero)
