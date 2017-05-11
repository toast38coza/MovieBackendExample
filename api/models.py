from django.db import models

from .managers import MovieManager

class Movie(models.Model):

    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    year = models.PositiveIntegerField(default=2017)

    backend_id = models.CharField(max_length=128, blank=True)
    backends = models.CharField(max_length=244) # commaseperated field -> ArrayField if we're using postgres

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = MovieManager()
