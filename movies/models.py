from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models


class Director(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.TextField(max_length=512, null=True, blank=True)
    profile_image = models.ImageField("image", upload_to="directors")

    class Meta:
        ordering = ["first_name"]
        verbose_name = "director"
        verbose_name_plural = "directors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.TextField(max_length=512, null=True, blank=True)
    profile_image = models.ImageField("image", upload_to="actors")

    class Meta:
        ordering = ["first_name"]
        verbose_name = "actor"
        verbose_name_plural = "actors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField(max_length=512, null=True, blank=True)
    url = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "genre"
        verbose_name_plural = "genres"

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=64)
    info = models.TextField(max_length=512)
    url = models.SlugField(max_length=100, unique=True)

    class Meta:

        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=512, null=True, blank=True)
    poster_image = models.ImageField("image", upload_to="movies")
    year = models.PositiveSmallIntegerField(default=2022)
    country = models.CharField(max_length=64)
    director = models.ManyToManyField(Director, related_name="film_director")
    actors = models.ManyToManyField(Actor, related_name="film_actor")
    genres = models.ManyToManyField(Genre, related_name="film_genre")
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0, help_text="price in dollars of USA")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "movie"
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title


class RaitingStars(models.Model):
    value = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "star of rating"
        verbose_name_plural = "stars of rating"

    def __str__(self):
        return self.value


class Rating(models.Model):
    ip = models.CharField(max_length=16)
    movie = models.ForeignKey(Movie, related_name="rating", on_delete=models.CharField)
    star = models.ForeignKey(
        RaitingStars, related_name="stars", on_delete=models.CharField
    )

    class Meta:
        verbose_name = "rating"
        verbose_name_plural = "rating"


class MovieShots(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=512, null=True, blank=True)
    image = models.ImageField(upload_to="movie_shots")
    id_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "shot from movie"
        verbose_name_plural = "shots from movie"

    def __str__(self):
        return self.title


class User(AbstractUser):
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username


class Reviews(models.Model):
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"

    def __str__(self):
        return f"{self.user} - {self.movie}"
