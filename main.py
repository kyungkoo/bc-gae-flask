from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
    return "It works!"


@app.route('/hello')
def hello_page():
    return "Hello Google App Engine with Flask!"
