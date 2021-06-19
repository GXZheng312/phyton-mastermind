import mastermind
from flask import render_template, redirect

def index():
    if mastermind.mastermind_game.player == None:
        return redirect('/load')

    mastermind.my_data.color_list = mastermind.app.game.board.COLORS
    
    return render_template('index.html', data=mastermind.my_data)