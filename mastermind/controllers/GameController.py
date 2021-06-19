import mastermind
from flask import render_template, redirect

def index():
    if mastermind.mastermind_game.player == None:
        return redirect('/load')

    myData = {
        'name': 'Jacky',
        'pets': ['doggo', 'cat', 'fish']
    }

    return render_template('index.html', data=myData)