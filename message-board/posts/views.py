from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts

class HomePageView(ListView):
    model = Posts
    template_name = "home.html"


# Create your views here.
