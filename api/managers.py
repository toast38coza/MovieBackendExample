from django.db import models

class MovieManager(models.Manager):

    def create_from_backend(self):
        pass

    def write_to_backend(self):
        pass