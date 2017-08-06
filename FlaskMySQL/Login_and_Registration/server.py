from flask import Flask, request, redirect, render_template, flash, session
import re
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'Login_and_Registration_db')
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['pwd']
    confirm_password = request.form['pwd_confirm']
    errors = False

    query = 'SELECT * FROM users WHERE email = :email'
    data = {
    'email': email
    }
    results = mysql.query_db(query, data)
    if len(results) > 0:
        flash('email already in use')
        return redirect('/')
    else:
        if len(first_name) < 2:
            flash('First name must be longer than 2 characters')
            errors = True
        if not first_name.isalpha():
            flash('First name can only contain letters')
            errors = True
        if len(last_name) < 2:
            flash('Last name must be longer than 2 characters')
            errors = True
        if not last_name.isalpha():
            flash('Last name can only contain letters')
            errors = True
        if not EMAIL_REGEX.match(email):
            flash('Invalid email address')
            errors = True
        if len(password) < 8:
            flash('Password must be 8 characters long')
            errors = True
        if password != confirm_password:
            flash('Passwords do not match')
            errors = True
        if errors:
            return redirect('/')
        else:
            pw_hash = bcrypt.generate_password_hash(password)
            insert_query = 'INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())'
            query_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'pw_hash': pw_hash
            }
            mysql.query_db(insert_query, query_data)
    flash('Please login')
    return redirect('/')

@app.route('/login/', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['pwd']
    query = 'SELECT * FROM users WHERE users.email = :email LIMIT 1'
    data = {
    'email': email
    }
    user = mysql.query_db(query, data)
    if user:
        session['user'] = mysql.query_db(query, data)
        if bcrypt.check_password_hash(session['user'][0]['pw_hash'], password):
            return redirect('/wall')
        else:
            flash('username or password is incorrect')
            return redirect('/')
    else:
        flash('username or password is incorrect')
        return redirect('/')

@app.route('/wall')
def wall():
    query = 'SELECT * FROM users JOIN messages ON users.id = messages.user_id ORDER BY messages.created_at DESC'
    messages = mysql.query_db(query)
    query = 'SELECT * FROM users JOIN comments on users.id = comments.user_id'
    comments = mysql.query_db(query)
    return render_template('wall.html', messages=messages, comments=comments)

@app.route('/logout', methods=['POST'])
def logoout():
    session.clear()
    return redirect('/')

@app.route('/message', methods=['POST'])
def message():
    message = request.form['message']
    if len(message) > 1:
        query = 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())'
        data = {
        'user_id': session['user'][0]['id'],
        'message': message
        }
        mysql.query_db(query, data)
        return redirect('/wall')
    else:
        flash('Can not leave an empy message!')
        return redirect('/wall')

@app.route('/comment/<message_id>', methods=['POST'])
def add_comment(message_id):
    comment = request.form['my_comment']
    query = 'INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW())'
    data = {
    'message_id': message_id,
    'user_id': session['user'][0]['id'],
    'comment': comment
    }
    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)
