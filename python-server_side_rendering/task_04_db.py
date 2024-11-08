from flask import Flask, render_template, request
import csv
import json
import sqlite3

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
    message = ""
    products = []
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv", "sql"]:
        message = "Wrong source"
    try:
        if source == "sql":
            conn = sqlite3.connect("products.db")
            cur = conn.cursor()

            if product_id:
                cur.execute("SELECT * FROM Products WHERE id=?", (product_id,))

            else:
                cur.execute("SELECT * FROM Products")

            sql_products = cur.fetchall()
            conn.close()

            # Convert list of tuples into list of dict
            products = [
                {
                    "id": tup_product[0],
                    "name": tup_product[1],
                    "category": tup_product[2],
                    "price": tup_product[3],
                }
                for tup_product in sql_products
            ]

        elif source == "json":
            with open("products.json", "r") as f:
                products = json.load(f)

        elif source == "csv":
            with open("products.csv", newline="") as f:
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

    except sqlite3.Error:
        message = "SQL request fails."

    except (FileNotFoundError, json.JSONDecodeError):
        message = "File not found."

    except Exception as e:
        message = f"An error occured:{e}"

    return render_template(
        "product_display.html", products=products, message=message
        )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
