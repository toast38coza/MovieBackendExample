from django.conf.urls import url
from rest_framework import routers, serializers, viewsets

from .models import Movie
from .serializers import MovieSerializer
from .mixins import BackendMixin

# Mixin order is important. Earlier takes precedence over later
class MovieViewSet(BackendMixin, viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)

