from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse("<b>Erx</b> Soft HUB!  2.0 Muraste ja Leo Serverid! 2022 <br><img src='https://1.bp.blogspot.com/-MO7J_n40P7s/YO1zC-avRbI/AAAAAAAANqc/JBiYjkinWAwdxGTyRcQVd7dFP6NHOAmfACLcBGAsYHQ/s685/computer-ads-families-1980s-17.jpg'>")
