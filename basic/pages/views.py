from django.shortcuts import render
from django.views.generic import TemplateView

def HomePageView(request):

    return render(request, "home.html")

def CountPageView(request):
    words = request.GET['counter']
    number_of_words = len(words.split())
    return render(request, "counter.html", {'count': number_of_words})


