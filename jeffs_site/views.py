from django.shortcuts import render

def index(request):
    """The home page for Jeff's Site"""
    return render(request, 'jeffs_site/index.html')
