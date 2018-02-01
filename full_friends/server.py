from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriends2db')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT name, age, friend_since FROM users")
    print friends
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO users (name, age, friend_since) VALUES (:name, :age, NOW())"
    data = {
             'name': request.form['name'],
             'age':  request.form['age']
           }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)