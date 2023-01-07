from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home_view"),
    path("about-me/", views.AboutView.as_view(), name="about_view"),
    path("contact-me/", views.ContactView.as_view(), name="contact_view"),
]
