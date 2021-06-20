import mastermind
from flask import render_template, request

def index():
    mastermind.my_data.all_players = mastermind.db.get_all_players()
    return render_template('leaderboard.html', data=mastermind.my_data)

