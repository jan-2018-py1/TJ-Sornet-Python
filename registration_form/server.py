from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "registrationform"

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def results():
    if len(request.form['email']) < 1:
        flash("Email address cannot be empty!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif len(request.form['first_name']) < 1:
        flash("First Name cannot be empty!")
    elif not request.form['first_name'].isalpha():
        flash("First Name can only contain letters!")
    elif len(request.form['last_name']) < 1:
        flash("Last Name cannot be empty!")
    elif not request.form['last_name'].isalpha():
        flash("Last Name can only contain letters!")
    elif len(request.form['password']) < 8:
        flash("Password must be more than 8 characters!")
    elif request.form['confirm_password'] != request.form['password']:
        flash("Passwords must match!")
    else: 
        return render_template('result.html')
    return redirect('/')

app.run(debug=True)