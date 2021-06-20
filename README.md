# Mastermind

Python Assignment 

## Installation

Go read the [installer](https://flask.palletsprojects.com/en/1.1.x/installation/#installation) manual.

To activate the environment (windows):
```powershell
venv\Scripts\activate
```
To run flask on development (windows):
```powershell
$evn:FLASK_ENV="development"
$env:FLASK_APP="setup.py"
flask run
```

## Usage

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, World!'
```
