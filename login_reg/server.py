from myconnection import MySQLConnector
from flask import Flask, render_template, request, redirect, session, flash
import re, md5
app = Flask(__name__)
app.secret_key = "My secret session key"
mysql = MySQLConnector(app, "login_reg_jan_2018")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def index():
	if "user_id" in session:
		return redirect('/success')
	return render_template("index.html")

@app.route('/success')
def success():
	query = "SELECT * FROM users WHERE id = :user_id"
	data = {
		"user_id": session['user_id']
	}
	user = mysql.query_db(query, data)[0]
	return render_template('success.html', user=user)


@app.route("/login", methods=["POST"])
def login():
	query = "SELECT * FROM users WHERE email = :email"
	data = {
		"email": request.form['email']
	}
	user = mysql.query_db(query, data)
	if user:
		user = user[0]
		if user['password'] == md5.new(request.form['password']).hexdigest():
			session['user_id'] = user['id']
			return redirect('/success')
	flash("No email and password combo found")
	return redirect('/')

@app.route("/register", methods=["POST"])
def register():
	dataIsValid = True
# First Name - letters only, at least 2 characters and that it was submitted
	if not request.form['first_name'].isalpha() or len(request.form['first_name']) < 2: 
		flash("First name must be at least 2 characters and contain only letters")
		dataIsValid = False
# Last Name - letters only, at least 2 characters and that it was submitted
	if not request.form['last_name'].isalpha() or len(request.form['last_name']) < 2: 
		flash("Last name must be at least 2 characters and contain only letters")
		dataIsValid = False
# Email - Valid Email format, and that it was submitted
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Email address not valid")
		dataIsValid = False
# Password - at least 8 characters, and that it was submitted
	if len(request.form['password']) < 8: 
		flash ("Password is too short")
		dataIsValid = False
# Password Confirmation - matches password
	if request.form['password'] != request.form['confirm']: 
		flash ("Password must match")
		dataIsValid = False
	if dataIsValid:
		query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:spot_one, :spot_two, :spot_three, :spot_four)"
		data = {
			'spot_one': request.form['first_name'],
			'spot_two': request.form['last_name'],
			'spot_three': request.form['email'],
			'spot_four': md5.new(request.form['password']).hexdigest()
		}
		myVar = mysql.query_db(query, data)
		session['user_id'] = myVar
		return redirect('/success')
	else:
		return redirect('/')

@app.route("/logout")
def logout():
	session.clear()
	return redirect("/")

app.run(debug=True)