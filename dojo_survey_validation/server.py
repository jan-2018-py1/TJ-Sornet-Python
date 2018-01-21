from flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)
app.secret_key = 'dojosurveyvalidation'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    location = request.form["place"]
    language = request.form["language"]
    if len(request.form["name"]) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    if len(request.form["comment"]) < 1:
        flash("Comments cannot be empty!")
        return redirect('/')
    if len(request.form['comment']) > 120:
            flash("Comments cannot be more than 120 characters!")
            return redirect('/')
    return render_template('result.html', names=names, location=location, language=language, comment=comment)

app.run(debug=True)