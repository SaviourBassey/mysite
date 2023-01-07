from django.shortcuts import render
from django.views import View

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/index.html")


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/about.html")


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/contact.html")

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        res = "Your Message has been sent successfully. I'll respond to you in a bit. Thanks!"
        context = {
            "res":res,
        }
        return render(request, "home/contact.html", context)