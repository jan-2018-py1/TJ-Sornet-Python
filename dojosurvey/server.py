from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    names = request.form["name"]
    location = request.form["place"]
    language = request.form["language"]
    comment = request.form["comment"]
    return render_template('result.html', names=names, location=location, language=language, comment=comment)

app.run(debug=True)