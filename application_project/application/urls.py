from django.urls import path
from .views import ApplicationCreateView

urlpatterns = [
    path('api/submit/', ApplicationCreateView.as_view(), name='api-submit'),
]