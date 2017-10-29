from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/survey', methods=['POST'])
def survey_data():
    print 'got post info'
    my_name = request.form['name']
    my_location = request.form['location']
    my_language = request.form['language']
    my_comment = request.form['comment']
    return render_template('result.html', my_name = my_name, my_location = my_location, my_language = my_language, my_comment = my_comment)
app.run(debug=True)
