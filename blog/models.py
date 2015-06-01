from django.db import models
from django.utils import timezone


class User(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
