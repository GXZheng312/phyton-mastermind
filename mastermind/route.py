from mastermind import controllers
from flask import Blueprint, render_template, redirect, request
import mastermind

web = Blueprint('web', __name__, static_folder='static', template_folder='templates')

@web.route('/')
def index():
    if mastermind.mastermind_game.player == None:
        return redirect('/load')
    return controllers.GameController.index()

@web.route('/leaderboard')
def leaderboard(): 
    return controllers.LeaderboardController.index()

@web.route('/load')
def load():
    return controllers.LoaderController.index()

@web.route('/setting')
def setting():
    return controllers.SettingController.index()

@web.route('/load-username')
def load_username():
    return controllers.LoaderController.loadUserName()

@web.route('/', defaults={'path': ''})
@web.route('/<path:path>')
def catch_all(path):
    return redirect('/') 