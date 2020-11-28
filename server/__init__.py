import os
from flask import Flask

"""
https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/
https://flask.palletsprojects.com/en/1.1.x/blueprints/#blueprints
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure
"""

def create_app(config=None):
    api = Flask(__name__)
    api.config.from_object(config)
    return api
