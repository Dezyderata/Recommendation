from django.contrib import admin
from recommendationApp.models import User, Movie, Rating

# Register your models here.

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Rating)
