from django.urls import path

from ..views.me import PrivateMovieDetail, PrivateMovieListCreateAPIView,MeDetail

urlpatterns = [
    path("",MeDetail.as_view(),name="me-detail"),
    path(
        "movies",
        PrivateMovieListCreateAPIView.as_view(),
        name="private-movie-list-create",
    ),
    path("movies/<int:id>", PrivateMovieDetail.as_view(), name="private-movie-detail"),
]
