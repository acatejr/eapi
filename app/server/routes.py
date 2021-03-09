from app.server import bp

@bp.route('/', methods=['GET'])
def index():
    return "welcome"

@bp.route('/status', methods=['GET'])
def status():
    return "ok"
