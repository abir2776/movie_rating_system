from rest_framework import generics

from movie_management.models import Movie

from ..serializers.movies import GlobalMovieSerializer,UserSerializer

from core.models import User


class PrivateMovieListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = GlobalMovieSerializer

    def get_queryset(self):
        return Movie.objects.filter(author=self.request.user)


class PrivateMovieDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GlobalMovieSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Movie.objects.filter(author=self.request.user)



class MeDetail(generics.ListAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    
