from flask.json import jsonify
from app.helper import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from flask import Flask, render_template, request
import os
import secrets
from datetime import timedelta
from flask_cors import CORS
from app.auth import auth, db
from app.web_routes import web_bp
from flask_jwt_extended import JWTManager


def create_app(test_config=None):
    app = Flask(
        __name__,
        instance_relative_config=True,
    )

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            # SQLALCHEMY_DATABASE_URI='postgresql://postgres:password@localhost:5432/kizito',
            SQLALCHEMY_DATABASE_URI="postgresql://neelxie:password@localhost:5433/kizito",
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY="1bSR#Nw00Y3axSjcjrXrU9Cs%_wJ7S",
        )
    else:
        app.config.from_mapping(test_config)

    app.config["STATIC_FOLDER"] = "static"
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=1)

    # allow cross-domain requests
    CORS(app)

    db.app = app
    db.init_app(app)

    JWTManager(app)

    app.register_blueprint(web_bp)
    app.register_blueprint(auth)

    @app.errorhandler(404)
    def handle_404(e):
        # Check if the request accepts JSON response
        if request.accept_mimetypes.accept_json:
            return jsonify({"error": "Route or Page not found"}), 404
        # For other formats (e.g., HTML), render the 404 template
        return render_template("404.html"), 404

    @app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
    def handle_500(e):
        return (
            jsonify({"error": "Something went wrong, we are working on it"}),
            HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
