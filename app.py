from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask import render_template
import requests

app = Flask(__name__, static_folder='./dist/static', template_folder='./dist')

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if app.debug:
        return requests.get('http://127.0.0.1:8080/{}'.format(path)).text
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

