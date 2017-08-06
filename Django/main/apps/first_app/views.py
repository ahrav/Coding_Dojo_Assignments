from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(requests):
    response = 'Hello, I am your first request!'
    return HttpResponse(response)
