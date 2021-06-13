import mastermind
from flask import Flask

app = Flask(__name__)

# ObjectClass = mastermind.app.module_one.ExampleClass() # import mastermind.blah.blah.blah
ObjectClass = mastermind.app.module_one.example.ExampleClass() # from * import package....

@app.route('/')
def hello_world():
    return ObjectClass.example