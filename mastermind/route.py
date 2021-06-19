from mastermind import controllers
from flask import Blueprint, redirect
\
web = Blueprint('web', __name__, static_folder='static', template_folder='templates')

@web.route('/')
def index():
    return controllers.GameController.index()

@web.route('/leaderboard')
def leaderboard(): 
    return controllers.LeaderboardController.index()

@web.route('/load')
def load():
    return controllers.LoaderController.index()

@web.route('/load-username')
def load_username():
    return controllers.LoaderController.load_username()

@web.route('/setting')
def setting():
    return controllers.SettingController.index()

@web.route('/save-setting')
def save_setting():
    return controllers.SettingController.save_setting()

@web.route('/', defaults={'path': ''})
@web.route('/<path:path>')
def catch_all(path):
    return redirect('/') 