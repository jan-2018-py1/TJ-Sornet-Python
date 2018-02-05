from mysqlconnection import MySQLConnector
from flask import Flask, render_template, redirect, session, flash, request, url_for
app = Flask(__name__)
app.secret_key = "83u4rjoif9"
mysql = MySQLConnector(app, "booksdb")

# a GET request to display all books. - DONE
@app.route('/')
def index():
    # query books table
    query = "SELECT * FROM books"
    all_books = mysql.query_db(query)
    return render_template('index.html', all_books=all_books)

# GET request to display a form allowing to add a new 
# book. - DONE
@app.route('/add')
def add():
    return render_template('add.html')

# POST to /create to insert a new book into our database. -DONE
@app.route('/create', methods=['POST'])
def create():
    query = "INSERT INTO books (title, author, created_at, updated_at) VALUES (:title, :author, NOW(), NOW());"
    data = {
        "title": request.form['title'],
        "author": request.form['author']
    }
    addBook = mysql.query_db(query, data)
    return redirect('/')

# GET request /users/<id>/edit - calls the edit method to display a form allowing users to 
# edit an existing user with the given id. This will need a template. - DONE
@app.route('/update/<id>')
def edit(id):
    query = 'SELECT * FROM books WHERE books.id = :id'
    data = {
        "id": id
    }
    getBook = mysql.query_db(query, data)[0]
    return render_template('update.html', getBook=getBook)

# POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. 
# Have this redirect to /users/<id> once updated. - DONE
@app.route('/users/<id>', methods=['POST'])
def update(id):
    query = "UPDATE books SET title = :title, author = :author WHERE id = :id"
    data = {
        "title": request.form['title'],
        "author": request.form['author'],
        "id": id
    }
    updateBook = mysql.query_db(query, data)
    return redirect('/')

@app.route('/destroy/<id>')
def destroy(id):
    query = "SELECT * FROM books WHERE id = :id"
    data = {
        "id": id
    }
    getBook = mysql.query_db(query, data)[0]
    return render_template('destroy.html', getBook=getBook)

# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. 
# Have this redirect back to /users once deleted. - DONE
@app.route('/destroy/<id>', methods=['POST'])
def delete(id):
    query = "DELETE FROM books WHERE id = :id"
    data = {
        "id": id
    }
    deleteUser = mysql.query_db(query, data)
    return redirect('/')



app.run(debug=True)