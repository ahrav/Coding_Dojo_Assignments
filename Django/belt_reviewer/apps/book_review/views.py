from django.shortcuts import render, redirect
from django.contrib import messages
from models import *

# Create your views here.
def index(request):
    context = {
        'recent': Review.objects.recent_and_old()[0],
        'rest': Review.objects.recent_and_old()[1]
    }
    return render(request, 'book_review/index.html', context)

def add(request):
    context = {
            'authors': Author.objects.all(),
        }
    return render(request, 'book_review/book.html', context)

def show(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'book_review/show.html', context)

def create(request):
    errors = Review.objects.validate_review(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
    else:
        Review.objects.create_review(request.POST, request.session['id'])
    return redirect('/books')
