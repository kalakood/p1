from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def homePageView(request):
    return HttpResponse("E!!!")

class HView(TemplateView):
    template_name = "home.html"
