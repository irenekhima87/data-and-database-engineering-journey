
import sqlite3
from datetime import datetime

DB_NAME = "inventory.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def low_stock_report(conn):
    print("\nLOW-STOCK REPORT")

    rows = conn.execute("""
        SELECT product_id, product_name, stock_quantity
        FROM Products
        WHERE stock_quantity < 5
    """).fetchall()

    for row in rows:
        print(row)

def record_sale(conn, product_id, customer_id, quantity):

    product = conn.execute("""
        SELECT product_name, stock_quantity
        FROM Products
        WHERE product_id = ?
    """, (product_id,)).fetchone()

    if product is None:
        print("Product not found.")
        return

    if product[1] < quantity:
        print("Not enough stock.")
        return

    conn.execute("""
        INSERT INTO Sales
        (product_id, customer_id, quantity_sold, sale_date)
        VALUES (?, ?, ?, ?)
    """, (
        product_id,
        customer_id,
        quantity,
        datetime.now()
    ))

    conn.execute("""
        UPDATE Products
        SET stock_quantity = stock_quantity - ?
        WHERE product_id = ?
    """, (quantity, product_id))

    conn.commit()

    print("Sale recorded successfully.")

def main():

    conn = get_connection()

    record_sale(
        conn,
        product_id=2,
        customer_id=1,
        quantity=1
    )

    low_stock_report(conn)

    conn.close()

if __name__ == "__main__":
    main()
