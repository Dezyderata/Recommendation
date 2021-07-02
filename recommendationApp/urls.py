from django.urls import path
from recommendationApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formpage/', views.form_user_view, name='form_name'),
]
