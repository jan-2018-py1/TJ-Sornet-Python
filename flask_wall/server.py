from mysqlconnection import MySQLConnector
from flask import Flask, render_template, request, session, redirect, flash
app = Flask(__name__)
app.secret_key = "alakj23aosdifasdf23"
mysql = MySQLConnector(app, "flask_wall")
import re, md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def index():
	if "user_id" in session:
		return redirect('/wall')
	return render_template("index.html")


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
            session['first_name'] = user['first_name']
            return redirect('/wall')
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
		query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:spot_one, :spot_two, :spot_three, :spot_four, NOW(), NOW())"
		data = {
			'spot_one': request.form['first_name'],
			'spot_two': request.form['last_name'],
			'spot_three': request.form['email'],
			'spot_four': md5.new(request.form['password']).hexdigest()
		}
		myVar = mysql.query_db(query, data)
		session['user_id'] = myVar
		session['first_name'] = request.form['first_name']
		return redirect('/wall')
	else:
		return redirect('/')

@app.route('/wall')
def wall():
	if "user_id" not in session:
		return redirect('/')
	printMessage = "SELECT first_name, last_name, message, DATE_FORMAT(messages.created_at, '%M %D %Y %T') as created_at, messages.id FROM users JOIN messages ON users.id = messages.user_id ORDER BY created_at DESC"
	post = mysql.query_db(printMessage)

	printComment = "SELECT first_name, last_name, comments.comment, comments.message_id, DATE_FORMAT(comments.created_at, '%M %D %Y %T') as created_at FROM users JOIN comments ON users.id = comments.user_id ORDER BY created_at DESC"
	comment = mysql.query_db(printComment)
	return render_template('wall.html', post=post, comment=comment)

@app.route("/message", methods=["POST"])
def message():
    getMessage = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:postedMessage, :userID, NOW(), NOW())"
    messageData = {
        "postedMessage": request.form['message'],
        "userID": session["user_id"]
    }
    message = mysql.query_db(getMessage, messageData)
    return redirect('/wall')

@app.route("/comment", methods=["POST"])
def comment():
    getComment = "INSERT INTO comments (comment, user_id, message_id, created_at, updated_at) VALUES (:postedComment, :userID, :messageID, NOW(), NOW())"
    commentData = {
        "postedComment": request.form['comment'],
        "userID": session["user_id"],
        "messageID": request.form["postID"]
    }
    comment = mysql.query_db(getComment, commentData)
    return redirect('/wall')

@app.route("/logout")
def logout():
	session.clear()
	return redirect("/")

app.run(debug=True)