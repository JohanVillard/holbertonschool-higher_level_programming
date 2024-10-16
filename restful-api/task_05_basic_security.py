#!/usr/bin/python3
"""This module defines security training."""

from flask_httpauth import HTTPBasicAuth
from flask import Flask, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt
from flask_jwt_extended import JWTManager

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

# Create a JWT manager
jwt = JWTManager(app)
app.config[
    "JWT_SECRET_KEY"
] = """d5836d17f93e24c72c1034c5ecec92698f7c5609a181ee723c79a77b43ee2c2c
06bb199c89d574e5209ba25e53416e2e12c1395e86c79426fb2ab2eeb1b0d8c156c48aa
ca783bb9649e43cac9c3a80b7408b19713a14b8c12720be428636f994f39e953ab61a5e
bfbd569a74f2a15b578ca95447c1bd3c36f19fafb1d154b1a7eed6edcc28cd56be6e005
e912cfff3c9d4a5cd75299faf776a16b375d4b736c5e330c69d50a8eaafb2dc14310d99
df1aabfe25e82af13f3f99fcb309697ed042778120489f95c392326254bb34758c39eb2
0f7db4e2cceaccb6be96198a0d388d039b6a7786a6fc019a8d95f66e6e5ab388e6ee539
6eb6756f860ad17fb900a2"""


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
    user = users.get(username)
    if username in users and check_password_hash(user["password"], password):
        return username
    else:
        return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required  # Access to indentified user only
def basic_protected():
    """Give access to web page to identified user."""
    return "Basic Auth: Access Granted", 200


@app.route("/login", methods=["POST"])
def login():
    """Check user's password."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if not verify_password(username, password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(
        identity=username, additional_claims={"role": user["role"]}
    )

    return jsonify(access_token=access_token), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()  # Protected by JWT
def jwt_protected():
    """Access to this route with JWT only."""
    return "JWT Auth: Access Granted", 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Access to admin only."""
    claims = get_jwt()
    if not claims["role"] == "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200


# jwt error handlers
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
    """
    Handle invalid JWT token errors.

    Parameters:
        err (Exception): The error that occured.

    Returns:
        tuple: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """
    Handle expired JWT token errors.

    Parameters:
        err (Exception): The error that occured.

    Returns:
        tuple: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """
    Handle errors indicating that a fresh JWT token is required.

    Parameters:
        err (Exception): The error that occured.

    Returns:
        tuple: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Fresh token required"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoke JWT token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


if __name__ == "__main__":
    app.run()
