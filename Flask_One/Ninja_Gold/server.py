from flask import Flask, render_template, session, redirect, request
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'Farm':
        farm_gold = random.randint(10,20)
        session['gold'] += farm_gold
        activity = 'You entered a farm, you earned ' + str(farm_gold) + ' golds from the farm! (' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')'
        session['activities'].append(activity)
        return redirect('/')
    elif request.form['building'] == 'Cave':
        cave_gold = random.randint(5,10)
        session['gold'] += cave_gold
        activity = 'You entered a cave, you earned ' + str(cave_gold) + ' golds from the cave! (' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')'
        session['activities'].append(activity)
        return redirect('/')
    elif request.form['building'] == 'House':
        house_gold = random.randint(2,5)
        session['gold'] += house_gold
        activity = 'You entered a house, you earned ' + str(house_gold) + ' golds from the house! (' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')'
        session['activities'].append(activity)
        return redirect('/')
    elif request.form['building'] == 'Casino':
        casino_gold = random.randint(-50,50)
        if casino_gold < 0:
            session['gold'] += casino_gold
            activity = 'You entered a casino, you lost ' + str(abs(casino_gold)) + ' golds from the casino!... Ouch! (' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')'
            session['activities'].append(activity)
            return redirect('/')
        elif casino_gold == 0:
            session['gold'] += casino_gold
            activity = 'you entered a casino, you did not win or lose any gold (' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')'
            return redirect('/')
        else:
            session['gold'] += casino_gold
            activity = 'You entered a casino, you earned ' + str(casino_gold) + ' golds from the casino.. Yaaay! (' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ')'
            session['activities'].append(activity)
            return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
