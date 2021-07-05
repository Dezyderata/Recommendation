from django.urls import path
from recommendationApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_page/', views.login_request, name='login_page'),
    path('registration_page/', views.register_user, name='registration_page'),
    path('main/', views.add_movie, name='main')
]
