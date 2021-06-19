import mastermind
from flask import render_template, request, redirect

def index():
    myData = {
        'name': 'Jacky',
        'pets': ['doggo', 'cat', 'fish']
    }

    return render_template('load.html', data=myData)

def loadUserName():
    username = request.args.get('username')
    mastermind.mastermind_game.setPlayer(username)

    return redirect('/')