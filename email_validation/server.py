from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "My secret session key"
mysql = MySQLConnector(app,'emaildb')
Email_key = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email', methods=['POST'])
def create():
    dataIsValid = True
    email = request.form["email"]
    if not Email_key.match(email):
	    flash("Email is not valid!")
	    dataIsValid = False
    if dataIsValid:
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
            'email': request.form['email']
        }
        mysql.query_db(query, data)
        session['email'] = request.form['email']
        return redirect('/success')
    else:
        return redirect('/')

@app.route('/success')
def success():
    emails = mysql.query_db("SELECT * FROM emails")
    currentEmail = emails[len(emails)-1]
    if emails:
        flash("The email address you entered {} is a VALID email address! Thank you!".format(currentEmail["email"]))
    return render_template('success.html', all_emails=emails)
app.run(debug=True)
