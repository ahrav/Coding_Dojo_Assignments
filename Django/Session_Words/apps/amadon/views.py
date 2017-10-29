from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'amadon/index.html')

def process_order(request):
    if request.POST['item'] == 'shirt':
        price = 19.99
    if request.POST['item'] == 'sweater':
        price = 29.99
    if request.POST['item'] == 'hat':
        price = 4.99
    if request.POST['item'] == 'book':
        price = 49.99

    item = {
    'quantity': request.POST['quantity'],
    'total_price': request.POST['quantity'] * price
    }

    item_list = request.session['items']
    item_list.append(item)
    request.session['items'] = item_list
    return redirect('/checkout')

def checkout(request):
    return render('amadon/checkout.html')
