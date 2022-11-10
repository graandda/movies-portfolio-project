from django.urls import path

from .views import MovieListView, MovieDetailView, register_request, login_request, logout_request, profile

urlpatterns = [
    path("", MovieListView.as_view(), name="index"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("register", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name="logout"),
    path("profile/", profile, name="user-profile")

]

app_name = "movies"
