from app.routes.auth_route import auth_bp
from app.routes.test_route import type_bp


def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(type_bp)

