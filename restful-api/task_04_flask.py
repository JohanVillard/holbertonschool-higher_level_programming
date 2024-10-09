#!/usr/bin/python3
"""This module defines basics of susage of Flask."""

from flask import Flask, jsonify, request

# Instantiate a Flask web server
app = Flask(__name__)
app.json.sort_keys = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
}


@app.route("/")
def home():
    """Return a string in home with Flask."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Return a JSON using jsonify."""
    # list keys of users
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Check status."""
    return "OK"


@app.route("/users/<username>")
def user_info(username):
    """
    Return the object corresponding to username.

    Parameters:
        username (str): The name of the object to return.

    Returns:
        obj
    """
    # Check if user exists
    for key, infos in users.items():
        if username == key:
            return jsonify(users[username])

    # User does not exist
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add an user in th user's dict."""
    # Parse the incoming json
    rq = request.get_json()

    # Extract the required fields
    username = rq.get("username")

    # Check is user is specified
    if username:
        name = rq.get("name")
        age = rq.get("age")
        city = rq.get("city")

        # Add the new user to the user's dict
        users[username] = {"username": username, "name": name, "age": age, "city": city}

        # Return a confirmation message
        return jsonify({"message": "User added", "user": users[username]}), 201

    else:
        # No user specified
        return jsonify({"error": "Username is required"}), 400


if __name__ == "__main__":
    app.run()
