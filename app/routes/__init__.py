def init_routes(app):
    from app.routes.categorize import categorize_bp

    app.register_blueprint(categorize_bp, url_prefix="/categorize")