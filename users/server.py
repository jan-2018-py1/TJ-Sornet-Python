from mysqlconnection import MySQLConnector
from flask import Flask, render_template, redirect, session, flash, request, url_for
app = Flask(__name__)
app.secret_key = "asdf23sdfa3"
mysql = MySQLConnector(app, "friendsdb")

# a GET request to /users - calls the index method to display all the users. This will need a template. - DONE
@app.route('/users')
def index():
    # query friends table
    query = "SELECT * FROM friends"
    all_users = mysql.query_db(query)
    return render_template('index.html', all_users=all_users)

# GET request to /users/new - calls the new method to display a form allowing users to create a new user. 
# This will need a template. - DONE
@app.route('/users/new')
def new():
    return render_template('new.html')

# GET request /users/<id>/edit - calls the edit method to display a form allowing users to 
# edit an existing user with the given id. This will need a template. - DONE
@app.route('/users/<id>/edit')
def edit(id):
    query = 'SELECT * FROM friends WHERE friends.id = :id'
    data = {
        "id": id
    }
    getUser = mysql.query_db(query, data)[0]
    return render_template('edit.html', getUser=getUser)

# GET /users/<id> - calls the show method to display the info for a particular user with given id. 
# This will need a template. - DONE
@app.route('/users/<id>')
def show(id):
    query = 'SELECT * FROM friends WHERE friends.id = :id'
    data = {
        "id": id
    }
    getUser = mysql.query_db(query, data)[0]
    return render_template('show.html', getUser=getUser)

# POST to /users/create - calls the create method to insert a new user record into our database. 
# This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created. - DONE
@app.route('/users/create', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW());"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
    }
    addUser = mysql.query_db(query, data)
    print addUser
    return redirect(url_for('show', id=addUser))

# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. 
# Have this redirect back to /users once deleted. - DONE
@app.route('/users/<id>/destroy')
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {
        "id": id
    }
    deleteUser = mysql.query_db(query, data)
    return redirect('/users')

# POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. 
# Have this redirect to /users/<id> once updated. - DONE
@app.route('/users/<id>', methods=['POST'])
def update(id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": id
    }
    updateUser = mysql.query_db(query, data)
    return redirect(url_for('show', id=id))

app.run(debug=True)
