import mastermind
from flask import Flask

app = Flask(__name__, static_folder='mastermind/static')
app.register_blueprint(mastermind.route.web)
