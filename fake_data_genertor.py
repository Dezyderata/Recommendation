import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieRecommendation.settings')

import django

django.setup()

import random
from recommendationApp.models import User, Rating, Movie
from faker import Faker

data_gen = Faker()


def add_user():
    fake_username = data_gen.name()
    fake_username = ''.join(fake_username.split())
    fake_passwd = data_gen.password()
    user = User.objects.get_or_create(user_name=fake_username, password=fake_passwd)[0]
    user.save()
    return user

def add_movie():
    fake_title = data_gen.name()
    movie = Movie.objects.get_or_create(movie_name=fake_title)[0]
    movie.save()
    return movie

def populate():
    movies = []
    users = []
    for item in range(30):
        movies.append(add_movie())
    for user in range(15):
        users.append(add_user())
    for item in range(70):
        rating_user = random.choice(users)
        rated_movie = random.choice(movies)
        rate = random.randint(1, 5)
        user_rating = Rating.objects.get_or_create(movie=rated_movie, user=rating_user, rate=rate)

if __name__ == '__main__':
    print("populating script!")
    populate()
    print("populating complete!")
