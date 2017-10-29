from django.shortcuts import render, HttpResponse, redirect
from django.db import models
from django.contrib import messages
from models import *
# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'course/index.html', context)

def delete(request, id):
    if request.method == 'GET':
        course = Course.objects.get(id=id)
        return render(request, 'course/delete.html', {'course': course})
    else:
        course = Course.objects.get(id=id)
        course.delete()
        return redirect('/')

def add(request):
    errors = Course.objects.validate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        Course.objects.create(name = request.POST['name'], description = request.POST['description'])
        return redirect('/')
