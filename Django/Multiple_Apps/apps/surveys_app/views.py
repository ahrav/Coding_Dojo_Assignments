from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def create(requests):
    response = "placeholder to display all the surveys created"
    return HttpResponse(response)

def add(requests):
    response = "placeholder for users to add a new survey"
    return HttpResponse(response)
