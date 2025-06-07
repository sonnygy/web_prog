from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('contacts/', views.contacts, name='contacts'),
    path('reviews/', views.reviews, name='reviews'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('initial_comments/', views.initial_comments, name='initial_comments'),
]

