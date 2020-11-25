from flask import Flask
import os
server = Flask(__name__)

@server.route("/")
def hello():
    print(os.getenv('FLASK_APP'))
    return "Hello everyone!"

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000)