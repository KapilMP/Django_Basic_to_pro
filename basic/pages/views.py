from django.shortcuts import render
from django.views.generic import TemplateView

def HomePageView(request):
    context ={
        "name" : "Patrick",
        "age" : 23,
        "nationality" : "Nepali",
    }
    return render(request, "home.html", context)


# Create your views here.
