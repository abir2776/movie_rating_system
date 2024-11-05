from rest_framework import generics
from rest_framework.permissions import AllowAny

from movie_management.choices import Status
from movie_management.models import Movie, Rating

from ..serializers.movies import GlobalMovieSerializer, ReviewRatingSerializer


class GlobalMovieList(generics.ListAPIView):
    queryset = Movie.objects.filter(status=Status.ACCEPTED)
    serializer_class = GlobalMovieSerializer
    permission_classes = [AllowAny]


class ReviewRatingListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReviewRatingSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        movie_id = self.kwargs.get("movie_id")
        movie = generics.get_object_or_404(
            Movie.objects.filter(), id=movie_id, status=Status.ACCEPTED
        )
        return Rating.objects.filter(movie=movie)


class GlobalMovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.filter(status=Status.ACCEPTED)
    serializer_class = GlobalMovieSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"
