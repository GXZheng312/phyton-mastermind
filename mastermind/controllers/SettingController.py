import mastermind
from flask import render_template, redirect, request

def index():
    return render_template('setting.html', data=mastermind.MyData)

def save_setting():
    print(request.args.get('isMultiColorOn'))

    mastermind.mastermind_game.isMultiColorOn = request.args.get('isMultiColorOn')
    mastermind.mastermind_game.amountOfColors = request.args.get('colors')
    mastermind.mastermind_game.board.positions = request.args.get('positions')

    return redirect('/setting')