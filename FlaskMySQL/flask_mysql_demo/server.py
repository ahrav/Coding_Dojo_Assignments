from flask import Flask, render_template
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'world')
# an example of running a query
@app.route('/countries/<limit>')
def countries(limit):
    query = "SELECT * FROM countries LIMIT :num"
    data = {
        'num' : int(limit)
    }
    countries = mysql.query_db(query, data)
    return render_template('countries.html', countries = countries)
app.run(debug=True)
