import mastermind
from flask import render_template, redirect

def index():
    if mastermind.mastermind_game.player == None:
        return redirect('/load')

    return render_template('index.html', data=mastermind.my_data)