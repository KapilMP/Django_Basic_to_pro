from django.urls import path
from .views import HomePageView, CountPageView

urlpatterns = [
    path("", HomePageView, name="home"),
    path("counter/", CountPageView, name="counter"),
]

