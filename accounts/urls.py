from django.urls import path
from .views import SignupView
from django.contrib.auth import urls


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup")
]
