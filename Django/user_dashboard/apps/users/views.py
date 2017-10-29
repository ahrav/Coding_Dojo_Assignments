from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def signin(request):
    return render(request, 'users/login.html')

def register(request):
    if request.method == 'GET':
        return render (request, 'users/register.html')
    else:
        errors = User.objects.validate_registration(request.POST)
        if errors:
            for error in errors:
                messages.error(reqeust, error)
            return redirect('/register')
        else:
            new_user = User.objects.create_user(request.POST)
            request.session['id'] = new_user.id
        return redirect('/login_success')

def login(request):
    results = User.objects.validate_login(request.POST)
    if results[0]:
        for error in results[0]:
            messages.error(request, error)
        return redirect('/signin')
    else:
        request.session['id'] = results[1].id
        return redirect('/login_success')

def login_success(request):
    if request.session['id'] == 1:
        return redirect('/dashboard/admin')
    else:
        return redirect('/dashboard')

def admin_dashboard(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'users/admin_dashboard.html', context)

def dashboard(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'users/dashboard.html', context)

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'users/show_user.html', context)

def delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/dashboard/admin')

def edit_user(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'users/edit_user.html', context)

def edit_info(request, user_id):
    errors = User.objects.validate_edit(request.POST)
    if errors:
        for error in errors:
            messages.error(reqeust, error)
        return redirect('/users/edit'+ user_id)
    else:
        updated_user = User.objects.edit_info(request.POST, user_id)
        messages.success(request, 'Successfully updated')
        return redirect('/dashboard/admin')

def update_password(request, user_id):
    errors = User.objects.validate_password_edit(request.POST)
    if errors:
        for error in errors:
            messages.error(reqeust, error)
        return redirect('/users/edit'+ user_id)
    else:
        updated_password = User.objects.update_password(request.POST, user_id)
        messages.success(request, 'Successfully updated')
        return redirect('/dashboard/admin')



def edit_self(request):
    if request.method == 'GET':
        context = {
            'user': User.objects.get(id=request.session['id'])
        }
        return render(request, 'users/edit_self.html', context)
    else:
        pass
