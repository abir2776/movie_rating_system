from django.urls import path

from ..views.admin import AdminMovieDetail, AdminMovieListCreateAPIView

urlpatterns = [
    path(
        "movies",
        AdminMovieListCreateAPIView.as_view(),
        name="admin-movie-list-create",
    ),
    path("movies/<int:id>", AdminMovieDetail.as_view(), name="admin-movie-detail"),
]
