from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'Newkey'


@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html', count=session['count'])

@app.route('/process', methods=['POST'])
def process():
    if request.form['action'] == 'increment':
        session['count'] += 1
    elif request.form['action'] == 'reset':
        session['count'] = 0
    return redirect('/')

app.run(debug=True)