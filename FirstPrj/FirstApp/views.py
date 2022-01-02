from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage_view(request):
    html = r'<!DOCTYPE html><html><head><title>'\
    + r'Frist Webapp Hello World'\
    + r'</title></head><body>'\
    + r'<h1>Hello World!</h1>'\
    + r'</body></html>'
    return HttpResponse(html)