import re
from mastermind.app.game.board import MAX_POSITION, MIN_POISTION
from mastermind.app.game import MAX_COLORS, MIN_COLORS
import mastermind
from flask import render_template, redirect, request

def index():
    return render_template('setting.html', data=mastermind.my_data)

def save_setting():
    multi_color = request.form.get('isMultiColorOn')
    colors = int(request.form.get('colors'))
    positions = int(request.form.get('positions'))

    mastermind.mastermind_game.multi_color = True if multi_color is not None else False

    if colors <= MAX_COLORS and colors >= MIN_COLORS: 
        mastermind.mastermind_game.amount_color = colors

    if positions <= MAX_POSITION and positions >= MIN_POISTION: 
        mastermind.mastermind_game.board.positions = positions

    return redirect('/setting')