from django.shortcuts import render


# Views for this project
def home(request):
    return render(request, "home.html")
