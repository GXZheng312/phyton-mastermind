from mastermind.app.game.board import MAX_POSITION, MIN_POISTION
from mastermind.app.game import MAX_COLORS, MIN_COLORS
import mastermind
from flask import render_template, redirect, request

def index():
    return render_template('setting.html', data=mastermind.my_data)

def save_setting():
    multi_color = request.args.get('isMultiColorOn')
    colors = int(request.args.get('colors'))
    positions = int(request.args.get('positions'))

    mastermind.mastermind_game.multi_color = multi_color

    if colors <= MAX_COLORS and colors >= MIN_COLORS: 
        mastermind.mastermind_game.amount_color = request.args.get('colors')

    if positions <= MAX_POSITION and positions >= MIN_POISTION: 
        mastermind.mastermind_game.board.positions = request.args.get('positions')

    return redirect('/setting')