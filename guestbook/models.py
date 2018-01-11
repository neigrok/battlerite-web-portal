from django.db import models


# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length=20)
    text = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author + ':' + self.text[:20]
