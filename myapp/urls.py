from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('contacts/', views.contacts, name='contacts'),
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('success/', views.success, name='success')
]
