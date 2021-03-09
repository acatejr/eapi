from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.server import bp as server_bp
    app.register_blueprint(server_bp)
    
    return app
