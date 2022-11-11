from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import generic

from .models import Movie, Genre, User, Actor, Director
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


def index(request):
    """View function for the home page of the site."""

    num_movies = Movie.objects.count
    num_genres = Genre.objects.count()
    num_users = User.objects.count()

    context = {
        "num_movies": num_movies,
        "num_genres": num_genres,
        "num_users": num_users,
    }

    return render(request, "movies/index.html", context=context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("movies:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/registration.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("movies:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("movies:index")


@login_required
def profile(request):
    return render(request, "movies/user_profile.html")


class MovieListView(generic.ListView):
    model = Movie
    context_object_name = "movie_list"
    template_name = "base.html"
    paginate_by = 10


class MovieListforallView(generic.ListView):
    model = Movie
    context_object_name = "movie_list"
    template_name = "movies/index.html"


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"


class ActorDetailView(generic.DetailView):
    model = Actor
    template_name = "movies/actor_detail.html"


class ActorListView(generic.ListView):
    model = Actor
    template_name = "movies/actor_list.html"


class DirectorDetailView(generic.DetailView):
    model = Director
    template_name = "movies/director_detail.html"


class DirectorListView(generic.ListView):
    model = Director
    template_name = "movies/director_list.html"
