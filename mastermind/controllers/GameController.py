from mastermind import db
import mastermind
from flask import render_template, redirect, request


def index():
    if mastermind.mastermind_game.player == None:
        return redirect('/load')

    if mastermind.my_data.status == "game ended":
        return redirect('/game/won')

    mastermind.my_data.color_list = mastermind.app.game.board.COLORS
    mastermind.my_data.status = "running"

    return render_template('index.html', data=mastermind.my_data)


def enable_cheat():
    mastermind.my_data.cheat_enabled = True

    return redirect('/')


def attempt():
    blocks = []

    for n in range(mastermind.mastermind_game.board.positions):
        block = request.form.get(f'block{n}')
        if block is not None:
            blocks.append(int(block))
        else:
            blocks.append(None)

    mastermind.mastermind_game.append_history(blocks)

    return redirect('/') if not check_win(blocks) else redirect('/game/won')


def check_win(blocks):
    for n in range(mastermind.mastermind_game.board.positions):
        if(blocks[n] != mastermind.mastermind_game.board.solution[n]):
            return False

    mastermind.my_data.status = "game won"
    return True


def won_screen():
    if mastermind.my_data.status == "game won":
        mastermind.mastermind_game.player.played += 1
        player_name = mastermind.mastermind_game.player.name
        turn_finished = len(mastermind.mastermind_game.board_history)
        cheated = mastermind.my_data.cheat_enabled
        db.save_player(player_name, turn_finished, cheated)
        mastermind.my_data.status = "game ended"

    if mastermind.my_data.status == "game ended":
        return render_template('won.html', data=mastermind.my_data)
    
    return redirect('/')


def reset():
    mastermind.mastermind_game.new_game()
    mastermind.my_data.cheat_enabled = False
    mastermind.my_data.status = "running"
    return redirect('/')
