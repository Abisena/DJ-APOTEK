from django.http import HttpResponse as response
from django.shortcuts import render

def home(request):
    # return response('Hello World')
    return render(request, 'home.html')
def about(request):
    # return response('Hello World')
    return render(request, 'about.html')