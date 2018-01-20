from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    string = "No ninjas here"
    return string

@app.route('/ninja')
def ninjas():
    return render_template("ninjas.html")

@app.route('/ninja/<color>')
def colors(color):
    if color == "blue":
        return render_template('blue.html')
    elif color == "orange":
        return render_template('orange.html')
    elif color == "red":
        return render_template('red.html')
    elif color == "purple":
        return render_template('purple.html')
    else:
        return render_template('notapril.html')

app.run(debug=True)