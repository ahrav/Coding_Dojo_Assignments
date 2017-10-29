from flask import Flask, session, request, redirect, render_template, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_form', methods=['POST'])
def register_form():
    if len(request.form['email']) < 1:
        flash('email can not be empty')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    if len(request.form['first_name']) < 1:
        flash('first name can not be empty')
        return redirect('/')
    elif request.form['first_name'].isalpha() == False:
        flash('first name can not contain numbers')
        return redirect('/')
    if len(request.form['last_name']) < 1:
        flash('last name can not be empty')
        return redirect('/')
    elif request.form['last_name'].isalpha() == False:
        flash('last name can not contain numbers')
        return redirect('/')
    if len(request.form['pwd']) < 8:
        flash('password must be at least 8 characters')
        return redirect('/')
    if not any(x.isupper() for x in request.form['pwd']) or not any(x.isdigit() for x in request.form['pwd']):
        flash('password needs one upper case letter and one number')
        return redirect('/')
    if len(request.form['pwd_confirm']) < 1:
        flash('password confirmation must be at least 8 characters')
        return redirect('/')
    if request.form['pwd'] != request.form['pwd_confirm']:
        flash('password and confirm password do not match')
        return redirect('/')
    # return render_template('submitted_form.html')
    return 'Thanks for submitting your information'

app.run(debug=True)
