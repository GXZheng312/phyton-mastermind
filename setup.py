import mastermind
from flask import Flask

app = Flask(__name__, static_folder='mastermind/static')
app.register_blueprint(mastermind.route.web)

# ObjectClass = mastermind.app.module_one.ExampleClass() # import mastermind.blah.blah.blah
# ObjectClass = mastermind.app.package_two.module_two.ClassTwo() # from * import package....

