from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "Ninjakey"
import random, time

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['won'] = 0
        session['message'] = [] 
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    now = time.ctime()
    if request.form['building'] == 'farm':
        session['won'] = random.randrange(10,21)
        activity = "Earned {} golds from the farm! ({})".format(session['won'], now)
    if request.form['building'] == 'cave':
        session['won'] = random.randrange(5,11)
        activity = "Earned {} golds from the cave! ({})".format(session['won'], now)
    if request.form['building'] == 'house':
        session['won'] = random.randrange(2,6)
        activity = "Earned {} golds from the house! ({})".format(session['won'], now)
    if request.form['building'] == 'casino':
        session['won'] = random.randrange(-50,51)
        if session['won'] < 0:
            activity = "Entered a casino and lost {} golds... Ouch.. ({})".format(session['won'], now)
        else:
            activity = "Earned {} golds from the casino! ({})".format(session['won'], now)
    session['gold'] += session['won']
    session['message'].insert(0, activity)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)