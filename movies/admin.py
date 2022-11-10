from django.contrib import admin
from .models import Category, Actor, Rating, RaitingStars, Reviews, Movie, MovieShots, Genre, Director


admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Actor)
admin.site.register(RaitingStars)
admin.site.register(Reviews)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Genre)
admin.site.register(Director)
