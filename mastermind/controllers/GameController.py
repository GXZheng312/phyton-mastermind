import mastermind
from flask import render_template, redirect, request

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
    blocks = []

    for n in range(mastermind.mastermind_game.board.positions):
        blocks.append(int(request.form.get(f'block{n}')))

    mastermind.mastermind_game.append_history(blocks)

    return redirect('/') if not check_win(blocks) else redirect('/game/won')

def check_win(blocks):
    for n in range(mastermind.mastermind_game.board.positions):
        if(blocks[n] != mastermind.mastermind_game.board.solution[n]):
            return False

    return True

def won_screen():
    # save player
    return render_template('won.html', data=mastermind.my_data)

def reset():
    # reset game 
    return redirect('/')