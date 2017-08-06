from flask import Flask, request, redirect, render_template, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'secret_key'
mysql = MySQLConnector(app, 'emails_db')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    session['email'] = request.form['email']
    if len(request.form['email']) < 1:
        flash('email can not be empty!')
        return redirect('/')
    elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        query = 'INSERT INTO emails (email_address, created_at, updated_at) VALUES (:email, NOW(), NOW())'
        data = {
        'email': request.form['email']
        }
        mysql.query_db(query, data)
        return redirect('/success')

@app.route('/success')
def success():
    query = 'SELECT email_address, MAX(created_at) as created_at FROM emails GROUP BY email_address ORDER BY created_at DESC'
    emails = mysql.query_db(query)
    return render_template('success.html', emails=emails)

app.run(debug=True)
