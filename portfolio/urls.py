from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.PortfolioHome.as_view(), name="portfolio_home"),
]
