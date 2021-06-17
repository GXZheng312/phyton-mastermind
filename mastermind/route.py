from mastermind import controllers
from flask import Blueprint, render_template

web = Blueprint('web', __name__, static_folder='static', template_folder='templates')

@web.route('/')
def index():
    myData = controllers.HomeController.index()
    
    return render_template('index.html', data=myData)

@web.route('/leaderboard')
def leaderboard():
    myData = controllers.HomeController.index()
    
    return render_template('index.html', data=myData)

