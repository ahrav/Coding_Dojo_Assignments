from django.shortcuts import render, HttpResponse, redirect
from buildings import buildings
import random
from datetime import datetime

# Create your views here.
def index(request):
    try:
        request.session['total_gold']
    except KeyError:
        request.session['total_gold'] = 0

    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []
    context = {
    'buildings': buildings
    }
    return render(request, 'ninja/index.html', context)

def process(request, building_id):
    for building in buildings:
        if building['id'] == int(building_id):
            if building['id'] ==1:
                farm_gold = random.randint(10,20)
                request.session['total_gold'] += farm_gold
                activity = 'You entered a farm, you earned ' + str(farm_gold) + ' golds from the farm! (' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')'
                activities = request.session['activities']
                activities.append(activity)
                request.session['activities'] = activities
                return redirect('/')
            elif building['id'] == 2:
                cave_gold = random.randint(5,10)
                request.session['total_gold'] += cave_gold
                activity = 'You entered a cave, you earned ' + str(cave_gold) + ' golds from the cave! (' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')'
                activities = request.session['activities']
                activities.append(activity)
                request.session['activities'] = activities
                return redirect('/')
            elif building['id'] == 3:
                house_gold = random.randint(2,5)
                request.session['total_gold'] += house_gold
                activity = 'You entered a house, you earned ' + str(house_gold) + ' golds from the house! (' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')'
                activities = request.session['activities']
                activities.append(activity)
                request.session['activities'] = activities
                return redirect('/')
            elif building['id'] == 4:
                casino_gold = random.randint(-50,50)
                if casino_gold < 0:
                    request.session['total_gold']+= casino_gold
                    activity = 'You entered a casino, you lost ' + str(abs(casino_gold)) + ' golds from the casino!... Ouch! (' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')'
                    activities = request.session['activities']
                    activities.append(activity)
                    request.session['activities'] = activities
                    return redirect('/')
                elif casino_gold == 0:
                    request.session['total_gold'] += casino_gold
                    activity = 'you entered a casino, you did not win or lose any gold (' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')'
                    activities = request.session['activities']
                    activities.append(activity)
                    request.session['activities'] = activities
                    return redirect('/')
                else:
                    request.session['total_gold'] += casino_gold
                    activity = 'You entered a casino, you earned ' + str(casino_gold) + ' golds from the casino.. Yaaay! (' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')'
                    activities = request.session['activities']
                    activities.append(activity)
                    request.session['activities'] = activities
                    return redirect('/')

def reset(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
