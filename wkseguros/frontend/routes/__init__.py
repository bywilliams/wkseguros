from .index_routes import index_bp


def register_routes(app):
    app.register_blueprint(index_bp)
