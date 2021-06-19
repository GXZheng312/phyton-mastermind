import mastermind
from flask import render_template, redirect

def index():
    if mastermind.mastermind_game.player == None:
        return redirect('/load')

    mastermind.my_data.color_list = mastermind.app.game.board.COLORS
    mastermind.my_data.status = "Running"
    
    return render_template('index.html', data=mastermind.my_data)

def enable_cheat():
    mastermind.my_data.cheat_enabled = True

    return redirect('/')

def attempt():

    return redirect('/')