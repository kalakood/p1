# pages/urls.py
from django.urls import path
from .views import homePageView
from .views import HView, AboutPageView
urlpatterns = [
    path("e/", homePageView, name="home_old"),
    path("cpc/", AboutPageView.as_view(), name="about"),
    path("about2/", AboutPageView.as_view(), name="about"),
    path("", HView.as_view(), name="home"),
]
