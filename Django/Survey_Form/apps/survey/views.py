from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'survey/index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    return redirect('/result')

def result(request):---
    return render(request, 'survey/result.html')

def reset(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
