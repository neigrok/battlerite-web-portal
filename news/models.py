from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from battlerite import settings

import cyrtranslit

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    #add tags

    class Meta:
        ordering = ['-timestamp', '-updated']

    def __str__(self):
        return self.title


def toppings_changed(sender, instance, **kwargs):
    transit_title = cyrtranslit.to_latin(instance.title, 'ru')
    instance.slug = slugify(transit_title, allow_unicode=True) + '-' + str(instance.pk)


pre_save.connect(toppings_changed, sender=News)
