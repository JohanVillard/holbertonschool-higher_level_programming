#!/usr/bin/python3
"""This module defines security training."""

from flask_httpauth import HTTPBasicAuth
from flask import Flask, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    JWTManager,
)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("hashed_password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("hashed_password"),
        "role": "admin",
    },
}

# Create a Flask server
app = Flask(__name__)

# Instance to add authentification based on HTTP
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "your_secret_key_here"

# Create a JWT manager
jwt = JWTManager(app)


@auth.verify_password
def verify_password(username, password):
    """
    Decode and check user's password.

    Parameters:
        username (str): The name of the user.
        password (str): The password of the user.

    Returns:
        username (str): The name of the user.
    """
    if username in users:
        user = users.get(username)
        if check_password_hash(user.get("password"), password):
            return username

    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required  # Access to indentified user only
def basic_protected():
    """Give access to web page to identified user."""
    return jsonify({"Basic Auth": "Access Granted"}), 200


@app.route("/login", methods=["POST"])
def login():
    """Check user's password."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not verify_password(username, password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)

    return jsonify(access_token=access_token), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()  # Protected by JWT
def jwt_protected():
    """Access to this route with JWT only."""
    return jsonify({"JWT Auth": "Access Granted"}), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Access to admin only."""
    username = get_jwt_identity()
    user = users.get(username)
    if not user.get("role") == "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"Admin Access": "Granted"}), 200


# -------------------------- jwt error handlers -------------------------- #


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle error for the request without token or invalid token.

    Parameters:
        err (str): The error message.

    Return:
        tuple: A response JSON with an error message et the status code 401.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle error for invalid token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired JWT token errors.

    Parameters:
        err (Exception): The error that occured.

    Returns:
        tuple: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle errors indicating that a fresh JWT token is required.

    Parameters:
        err (Exception): The error that occured.

    Returns:
        tuple: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Fresh token required"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoke JWT token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.token_verification_failed_loader
def handle_claims_check_error(err):
    """Handle claims check fails."""
    return jsonify({"error": "Claims check fails"}), 401


if __name__ == "__main__":
    app.run()
