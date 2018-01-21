from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'Numkey'

@app.route('/')
def index():
    if 'compNum' not in session:
        session['compNum'] = random.randrange(1, 101)
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'compNum' not in session:
        session['compNum'] = random.randrange(1, 101)
    session['message'] = ''
    session['player_guess'] = int(request.form['guessnumber'])
    session['compNum'] = random.randrange(1, 101)
    if session['compNum'] > session['player_guess']:
        session['message'] = "Too low!"
    if session['compNum'] < session['player_guess']:
        session['message'] = "Too high!"
    return redirect('/')

@app.route('/playagain', methods=['POST'])
def playagain():
    if 'compNum' not in session:
        session['compNum'] = random.randrange(1, 101)
    session['compNum'] = -1
    session.pop('player_guess')
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)