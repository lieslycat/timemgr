from flask import Flask

def create_app(config=None):
    app = Flask(__name__)
    if  not config:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_mapping(config)

