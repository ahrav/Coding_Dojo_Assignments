from django.shortcuts import render, redirect
from django.contrib import messages
from models import *

# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')

def register(request):
    errors = User.objects.validate_registration(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        new_user = User.objects.create_user(request.POST)
        request.session['id'] = new_user.id
        messages.success(request, 'Welcome, {}'.format(new_user.name))
    return redirect('/books')

def login(request):
    results = User.objects.validate_login(request.POST)
    if results[0]:
        for error in results[0]:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['id'] = results[1].id
        messages.success(request, 'Welcome, {}'.format(results[1].name))
        return redirect('/books')
