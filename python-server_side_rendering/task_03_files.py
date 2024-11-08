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
    source = request.args.get("source", "")
    if source is None:
        return render_template("product_display.html", products="Bad request."), 400

    product_id = request.args.get("id" None)

    if source == "json":
        try:
            with open("products.json", "r") as f:
                products = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return render_template(
                "product_display.html", products="Invalid json file."
            ), 404

    elif source == "csv":
        try:
            with open("products.csv", newline="") as f:
                csv_reader = csv.DictReader(f)
                raw_products = [row for row in csv_reader]

                # Delete whitespace generated by csv
                products = []
                for raw_product in raw_products:
                    product = {k: v.strip() for k, v in raw_product.items()}
                    products.append(product)
        except FileNotFoundError:
            return render_template(
                "product_display.html", products="Invalid CSV file."
            ), 404

    else:
        return render_template("product_display.html", products="Wrong source"), 400

    if not product_id:
        return render_template("product_display.html", products=products)

    # Build the dict in a list by id
    products = [product for product in products if str(product["id"]) == product_id]

    # Error if user specified an id which is not in database
    if not products:
        return render_template(
            "product_display.html", products="Product not found"
        ), 404

    return render_template("product_display.html", products=products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
