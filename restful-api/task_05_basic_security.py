#!/usr/bin/python3
"""This module defines security training."""

from functools import wraps

from flask_httpauth import HTTPBasicAuth
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("hello"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("bye"),
        "role": "admin",
    },
}

# Create a Flask server
app = Flask(__name__)

# Instance to add authentification based on HTTP
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = (
    """d5836d17f93e24c72c1034c5ecec92698f7c5609a181ee723c79a77b43ee2c2c06bb199c89d
574e5209ba25e53416e2e12c1395e86c79426fb2ab2eeb1b0d8c156c48aaca783bb9649e43cac9c3a8
0b7408b19713a14b8c12720be428636f994f39e953ab61a5ebfbd569a74f2a15b578ca95447c1bd3c3
6f19fafb1d154b1a7eed6edcc28cd56be6e005e912cfff3c9d4a5cd75299faf776a16b375d4b736c5e
330c69d50a8eaafb2dc14310d99df1aabfe25e82af13f3f99fcb309697ed042778120489f95c392326
254bb34758c39eb20f7db4e2cceaccb6be96198a0d388d039b6a7786a6fc019a8d95f66e6e5ab388e6
ee5396eb6756f860ad17fb900a2"""
)
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
    user = users.get(username)
    if username in users and check_password_hash(user["password"], password):
        print("Password verified")
        return username
    else:
        print("Bad login or bad password")
        return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required  # Access to indentified user only
def basic_protected():
    """Give access to web page to identified user."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Check user's password."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not verify_password(username, password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(
        identity=username,
        # Add admin flag in JWT
        additional_claims={
            "is_administrator": users[username]["role"] == "admin"
            },
    )
    return jsonify(access_token=access_token), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()  # Protected by JWT
def jwt_protected():
    """Access to this route with JWT only."""
    return "JWT Auth: Access Granted", 200


# Create a custom decorator
def admin_required():
    """
    Is Decorator to restrict access to routes to administrators only.

    Returns:
        function: A decorator that wraps the original function,
                  providing administrator access control.
    """

    def wrapper(fn):
        """
        Check condition to execute the original function.

        This function is called in place of the original function when
        the route is accessed. It verifies the JWT and checks if the user
        is an administrator.

        Parameters:
            fn (function): The original function to be decorated.

        Returns:
            function: The decorated function if the user is an
                      administrator; otherwise, a JSON response with
                      an error message and a 403 status code.
        """

        @wraps(fn)
        def decorator(*args, **kwargs):
            """
            Execute the original function if the user is an administrator.

            Parameters:
                *args: Positional arguments passed to the original function.
                **kwargs: Keyword arguments passed to the original function.

            Returns:
                fn (func): The original function's response if the user is
                           an administrator; otherwise, a JSON response
                           with an error message and a 403 status code.
            """
            # Check if JWT token is valid
            verify_jwt_in_request()
            # Get datas in JWT
            claims = get_jwt()
            # Administrator check
            if claims["is_administrator"]:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Admin only!"), 403

        return decorator

    return wrapper


@app.route("/admin-only", methods=["GET"])
@admin_required()  # Protect this route with admin_required decorator
def admin_only():
    """Access to admin only."""
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(debug=True)
