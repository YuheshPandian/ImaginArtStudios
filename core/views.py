from django.shortcuts import render
from django.http import HttpResponse


# Views for this project
def home(request):
    return HttpResponse("helllo world")
