from django.urls import path

from .views import (
    MovieListView,
    MovieDetailView,
    register_request,
    login_request,
    logout_request,
    profile,
    ActorDetailView,
    DirectorDetailView,
    ActorListView,
    DirectorListView,
)

urlpatterns = [
    path("", MovieListView.as_view(), name="index"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name="logout"),
    path("profile/", profile, name="user-profile"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actor/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("directors/", DirectorListView.as_view(), name="director-list"),
    path("director/<int:pk>/", DirectorDetailView.as_view(), name="director-detail"),
]

app_name = "movies"
