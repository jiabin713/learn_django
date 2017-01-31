from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    content_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', content_dict)


def about(request):
    content_dict = {}
    return render(request, 'rango/about.html', content_dict)