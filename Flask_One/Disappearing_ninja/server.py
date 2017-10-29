from flask import Flask, render_template, session, request, flash, redirect
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return 'No Ninjas Here!'

@app.route('/ninja')
def ninja():
    session['allNinjas'] = True
    return render_template('ninja.html')

@app.route('/ninja/<ninja_color>')
def single_ninja(ninja_color):
    session['allNinjas'] = False
    if ninja_color == 'orange':
        session['ninja'] = 'michelangelo'
    elif ninja_color == 'blue':
        session['ninja'] = 'leonardo'
    elif ninja_color == 'purple':
        session['ninja'] = 'donatello'
    elif ninja_color == 'red':
        session['ninja'] = 'raphael'
    else:
        session['ninja'] = 'other'
    return render_template('ninja.html')

app.run(debug=True)
