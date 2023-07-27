# admin_decorator.py

from functools import wraps
from flask import request, jsonify, current_app
from app.models import User, db
from flask_jwt_extended import decode_token


def clean_token(token):
    if token.startswith("Bearer "):
        token = token.split(" ")[1]
    return token


def get_authenticated_user():
    token = request.headers.get("Authorization")  # Example for token from headers

    if not token:
        return None


    cleaned_token = clean_token(token)
    decoded_token = decode_token(cleaned_token)
    user_id = decoded_token["sub"]

    # Fetch the user from the database based on the user_id in the token
    user = User.query.get(user_id)
    if user:
        return user.__dict__
    else:
        return None


def admin_required(endpoint):
    @wraps(endpoint)
    def wrapper(*args, **kwargs):
        user = get_authenticated_user()
        
        picked_role = user["role"]
        if not user:
            return jsonify({"error": "Unauthorized"}), 401

        if picked_role != "admin":
            return jsonify({"error": "Admin access required"}), 403

        return endpoint(*args, **kwargs)

    return wrapper
