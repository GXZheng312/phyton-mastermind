import mastermind
from flask import render_template

def index():
    

    return render_template('setting.html', data=mastermind.MyData)