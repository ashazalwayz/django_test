from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>This is the Home page.</h1>')

def about(request):
    return HttpResponse('<h1>This is the About page.</h1>')

def contact(request):
    return HttpResponse('<h1>This is the Contact page.</h1>')