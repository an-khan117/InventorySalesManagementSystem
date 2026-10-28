
from flask import Flask, render_template
from db import get_db_connection

app = Flask(__name__)


@app.route("/")
def dashboard():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                p.product_id,
                p.product_name,
                c.category_name,
                p.purchase_price,
                p.selling_price,
                p.stock_quantity,
                p.reorder_level
            FROM products AS p
            JOIN categories AS c
                ON p.category_id = c.category_id
            ORDER BY p.product_id
        """)

        products = cursor.fetchall()

        total_products = len(products)
        total_stock = sum(p["stock_quantity"] for p in products)
        low_stock = sum(
            1 for p in products
            if p["stock_quantity"] <= p["reorder_level"]
        )

        return render_template(
            "products.html",
            products=products,
            total_products=total_products,
            total_stock=total_stock,
            low_stock=low_stock
        )

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    app.run(debug=True)
