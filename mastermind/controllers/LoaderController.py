from mastermind import db
import mastermind
from flask import render_template, request, redirect


def index():
    return render_template('load.html', data=mastermind.my_data)


def load_username():
    username = request.args.get('username')
    found_player = db.get_player(username)
    amount_played = 0 if found_player is None else len(found_player['games'])

    mastermind.mastermind_game.set_player(username)
    mastermind.mastermind_game.player.played = amount_played
    mastermind.my_data.cheat_enabled = False
    mastermind.my_data.status = "loading player"

    return redirect('/')
