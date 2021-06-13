from flask import Flask
# from mastermind.app.test.example import ExampleClass

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hi"