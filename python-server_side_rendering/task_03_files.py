from flask import Flask, render_template, json, request, abort
import csv

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
    with open("items.json", "r") as f:
        items_list = json.load(f)

    return render_template("items.html", items=items_list["items"])


@app.route("/products")
def products():
    source = request.args.get("source")
    if source is None:
        abort(400)

    product_id = request.args.get("id")
    if id is None:
        abort(400)

    if source == "json":
        try:
            with open("products.json", "r") as f:
                products = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return render_template("product_display.html", products=products)

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
            return render_template("product_display.html", products=products)

    else:
        return render_template("product_display.html", products="Wrong source"), 400

    if not product_id:
        return render_template("product_display.html", products=products)

    for product in products:
        if str(product["id"]) == product_id:
            return render_template("product_display.html", products=[product])

    return render_template("product_display.html", products="Product not found"), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
