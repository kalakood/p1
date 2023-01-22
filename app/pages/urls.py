# pages/urls.py
from django.urls import path
from .views import homePageView
from .views import HView
urlpatterns = [
    path("e/", homePageView, name="home_old"),
    path("", HView.as_view(), name="home"),
]
