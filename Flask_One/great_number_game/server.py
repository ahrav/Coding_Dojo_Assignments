from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods= ['POST'])
def guess():
    if 'rand' not in session:
        session['rand'] = random.randrange(1,101)
    guess = int(request.form['number'])

    if guess < session['rand']:
        session['guess'] = 'too low'
    elif guess > session['rand']:
        session['guess'] = 'too high'
    else:
        session['guess'] = 'correct!'
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()
    return redirect('/')


app.run(debug = True)
