from django.urls import path
from core import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("about/", views.home, name="about"),
    path("contact/", views.home, name="contact"),
    path("testimonials/", views.home, name="testimonials"),
    path("services/", views.home, name="services"),
]
