import requests
from ..models import Movie

class OMDBBackend:
    '''OMDB backend handles '''

    def __to_movie(self, result):
        movie = Movie()
        movie.backend_id = result.get('imdbID')
        movie.name = result.get('Title')
        return movie


    def get_object(self, **kwargs):
        '''
        function responsible for getting a movie from IMDB
        '''
        id = kwargs.get('pk')
        url = 'http://www.omdbapi.com/?i={}'.format(id)
        result = requests.get(url)
        if result.status_code == 200:
            return self.__to_movie(result.json())
        else:
            # throw validation error
            pass
