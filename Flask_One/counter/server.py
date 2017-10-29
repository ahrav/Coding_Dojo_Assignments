from flask import Flask, request, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html')

@app.route('/button', methods=['POST'])
def plus_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
