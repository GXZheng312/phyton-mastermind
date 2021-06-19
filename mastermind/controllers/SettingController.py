from werkzeug.utils import redirect
import mastermind
from flask import render_template

def index():
    return render_template('setting.html', data=mastermind.MyData)

def save_setting():
    return redirect('/')