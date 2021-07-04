from django.test import TestCase
from recommendationApp.models import Movie, User, Rating
# Create your tests here.


class MovieTestCase(TestCase):

    def test_movie_str(self):
        first_movie = Movie.objects.create(movie_name="Scary Movie")
        self.assertEqual(first_movie.__str__(), "Scary Movie")


class UserTestCase(TestCase):

    def test_user_str(self):
        first_user = User.objects.create(username="Jose")
        self.assertEqual(first_user.__str__(), "Jose")
