from mastermind import controllers
from flask import Blueprint, redirect

web = Blueprint('web', __name__, static_folder='static',
                template_folder='templates')


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


@web.route('/save-setting', methods=['GET', 'POST'])
def save_setting():
    return controllers.SettingController.save_setting()


@web.route('/game/enable-cheat')
def enable_cheat():
    return controllers.GameController.enable_cheat()


@web.route('/game/send-attempt', methods=['GET', 'POST'])
def send_attempt():
    return controllers.GameController.attempt()


@web.route('/game/won')
def win():
    return controllers.GameController.won_screen()


@web.route('/game/reset')
def reset():
    return controllers.GameController.reset()


@web.route('/', defaults={'path': ''})
@web.route('/<path:path>')
def catch_all(path):
    return redirect('/')
