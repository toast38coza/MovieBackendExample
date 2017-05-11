'''
This is a mixin which we drop into our ViewSets to make them use a backend to overwrite the base methods
'''
import requests
from .models import Movie
from .backends.apibackend import APIBackend

class BackendMixin:
    '''Backend mixin handles proxying requests between API object models and entities on the specific backend'''

    def get_object(self):

        # get backend, get_object
        return APIBackend()\
                .get_backend('imdb')\
                .get_object(**self.kwargs)