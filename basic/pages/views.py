from django.shortcuts import render
# from django.views.generic import TemplateView
from .models import feature

def HomePageView(request):
    feature1 = feature()
    feature1.id = 1
    feature1.name = "Harry"
    feature1.details ="We are quick"

    feature2 = feature()
    feature2.id = 2
    feature2.name = "Prakash"
    feature2.details ="We are quicker"

    features = [feature1, feature2]

    return render(request, "home.html", {'feature': features})

def CountPageView(request):
    words = request.POST['counter']
    number_of_words = len(words.split()) if words else 0
    return render(request, "counter.html", {'count': number_of_words})


