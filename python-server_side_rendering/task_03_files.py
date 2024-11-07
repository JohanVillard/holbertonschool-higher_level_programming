from flask import Flask, render_template, json, request
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
    product_id = request.args.get("id")

    if source.endswith("json"):
        with open(source, "r") as f:
            products = json.load(f)

    elif source.endswith("csv"):
        with open("products.csv", newline="") as f:
            csv_reader = csv.DictReader(f)
            products = [row for row in csv_reader]

    else:
        return render_template("product_display.html", products="Wrong source"), 400

    if not product_id:
        return render_template("product_display.html", products=products)

    for raw_product in products:
        # Delete whitespace generated by csv
        product = {k: v.strip() for k, v in raw_product.items()}

        if str(product["id"]) == product_id:
            product_by_id = []
            product_by_id.append(product)
            return render_template("product_display.html", products=product_by_id)

    else:
        return render_template(
            "product_display.html", products="Product not found"
        ), 400


if __name__ == "__main__":
    app.run(debug=True, port=5000)
