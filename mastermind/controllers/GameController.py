from flask import render_template

def index():
    myData = {
        'name': 'Jacky',
        'pets': ['doggo', 'cat', 'fish']
    }

    return render_template('index.html', data=myData)