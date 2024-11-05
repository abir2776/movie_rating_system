from django.urls import path

from ..views.movies import (
    GlobalMovieDetailView,
    GlobalMovieList,
    ReviewRatingListCreateAPIView,
)

urlpatterns = [
    path("movies", GlobalMovieList.as_view(), name="global-movie-list"),
    path(
        "movies/<int:movie_id>/ratings",
        ReviewRatingListCreateAPIView.as_view(),
        name="review-rating-list-create",
    ),
    path(
        "movies/<int:id>", GlobalMovieDetailView.as_view(), name="global-movie-detail"
    ),
]
