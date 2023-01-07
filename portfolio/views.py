from django.shortcuts import render
from django.views import View
from .models import Portfolio

# Create your views here.

class PortfolioHome(View):
    def get(self, request, *args, **kwargs):
        all_portfolio = Portfolio.objects.all().order_by("-timestamp")
        context = {
            "all_portfolio":all_portfolio,
        }
        return render(request, "portfolio/portfolio.html", context)