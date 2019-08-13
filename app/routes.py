from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Miguel"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': "Hello there 1!!!"
        },
        {
            'author': {'username': 'Steve'},
            'body': "Hello there 2!!!"
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)