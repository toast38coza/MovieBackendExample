'''
The interface to backend services
'''
from django.utils.module_loading import import_string

# here is whare you would map what is stored on Movie.backends to a backend handler
backend_map = {
    'imdb': 'api.backends.omdb.OMDBBackend'
}

class APIBackend:
    '''A class responsible for creating the correct backend handler to handle the request'''

    def get_backend(self, backend_id):
        import_path = backend_map.get(backend_id)
        backend = import_string(import_path)
        return backend()

