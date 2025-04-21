# from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    # return HttpResponse("How to choose and how to cook potatoes: tips from the chef!")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("About Page")
    return render(request, 'about.html')

