from flask import Flask, render_template, redirect, session, flash, request
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dojo_survey', methods=['POST'])
def dojo_survey():
    if len(request.form['name']) < 1:
        flash('Name cannot be empty!')
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    if len(request.form['comment']) < 1:
        flash('Comment cannot be empty!')
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash('Comment can not be longer than 120 characters')
        return redirect('/')
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/back', methods=['POST'])
def back():
    return redirect('/')

app.run(debug=True)
