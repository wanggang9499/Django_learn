from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('<h1>hello world! store page</h1>')


def about(request):
    return HttpResponse('<h1>test store page!</h1>')

