from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/items")
def items():
    try:
        with open("items.json", "r") as f:
            data = json.load(f)
            items_list = data.get("items")

    except FileNotFoundError:
        items_list = []

    return render_template("items.html", items=items_list)


@app.route("/products")
def products():
    products = []
    message = None

    source = request.args.get("source", "")

    product_id = request.args.get("id", None)

    if source not in ["json", "csv"]:
        message = "Wrong source"

    try:
        if source == "json":
            with open("products.json", "r") as f:
                products = json.load(f)

        if source == "csv":
            with open("products.csv", "r") as f:
                csv_reader = csv.DictReader(f)
                products = [row for row in csv_reader]

        if product_id:
            # Build the dict in a list by id
            products = [
                product for product in products
                if str(product["id"]) == product_id
            ]

            # Error if user specified an id which is not in database
            if not products:
                message = "Product not found"

    except FileNotFoundError:
        message = "File not found."

    except Exception as e:
        message = f"An error occured: {e}"

    return render_template(
        "product_display.html", products=products, message=message
        )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
