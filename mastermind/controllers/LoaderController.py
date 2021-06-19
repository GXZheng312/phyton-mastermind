import mastermind
from flask import render_template, request, redirect

def index():
    return render_template('load.html', data=mastermind.my_data)

def load_username():
    username = request.args.get('username')
    mastermind.mastermind_game.setPlayer(username)

    return redirect('/')