import mastermind
from flask import render_template

def index():
    return render_template('leaderboard.html', data=mastermind.my_data)

