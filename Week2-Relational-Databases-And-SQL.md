Week 2: Relational Databases and SQL

1. Introduction

This project demonstrates the implementation of a relational database using SQLite. The database uses multiple related tables to organize users, products, and orders. Primary keys and foreign keys are used to establish relationships between the tables and maintain data integrity.

The project also demonstrates SQL queries, JOIN operations, sales calculations, inventory reporting, and Python integration with the database.

2. Database Schema

The database consists of three main tables:

- Users – stores information about customers.
- Products – stores information about products and inventory.
- Orders – stores customer orders and connects users with products.

Users Table

The Users table contains customer information.

The primary key is "user_id", which uniquely identifies each user.

Products Table

The Products table contains product information, including product names, prices, and available stock.

The primary key is "product_id", which uniquely identifies each product.

Orders Table

The Orders table stores information about purchases made by users.

The Orders table uses foreign keys to connect orders to users and products.

3. Primary and Foreign Keys

Primary keys uniquely identify records within a table.

For example:

user_id INTEGER PRIMARY KEY

Foreign keys create relationships between tables.

For example:

user_id INTEGER,
product_id INTEGER,
FOREIGN KEY (user_id) REFERENCES Users(user_id),
FOREIGN KEY (product_id) REFERENCES Products(product_id)

This ensures that orders are associated with existing users and products.

4. Database Normalization

The database follows basic normalization principles.

First Normal Form (1NF)

Each table contains atomic values, and each column stores a single type of information.

Second Normal Form (2NF)

Each non-key attribute depends on the primary key of its table.

Third Normal Form (3NF)

Non-key attributes depend only on the primary key and are not unnecessarily repeated across tables.

Separating users, products, and orders reduces data duplication and improves data consistency.

5. SQL Queries

JOIN Query

A JOIN can be used to combine information from the Users, Products, and Orders tables.

SELECT
    Users.user_id,
    Users.name,
    Products.product_name,
    Products.price,
    Orders.quantity
FROM Orders
JOIN Users ON Orders.user_id = Users.user_id
JOIN Products ON Orders.product_id = Products.product_id;

This query combines customer, product, and order information into one result.

Sales Calculation

The total value of an order can be calculated by multiplying the product price by the quantity ordered.

SELECT
    Orders.order_id,
    Products.product_name,
    Orders.quantity,
    Products.price,
    Orders.quantity * Products.price AS total_sales
FROM Orders
JOIN Products
ON Orders.product_id = Products.product_id;

Total Sales

The total sales value can be calculated using:

SELECT
    SUM(Orders.quantity * Products.price) AS total_sales
FROM Orders
JOIN Products
ON Orders.product_id = Products.product_id;

6. Automated Inventory Report

An inventory report can be created using a SQL view.

CREATE VIEW Sales_Report AS
SELECT
    Products.product_id,
    Products.product_name,
    Products.price,
    Products.stock,
    Orders.order_id,
    Orders.quantity,
    Orders.quantity * Products.price AS total_sales
FROM Products
JOIN Orders
ON Products.product_id = Orders.product_id;

The "Sales_Report" view automatically combines product and order information and calculates the sales value.

The report can then be viewed using:

SELECT *
FROM Sales_Report;

7. Python Database Integration

Python can be used to connect to the SQLite database and execute SQL queries.

import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute("""
SELECT *
FROM Sales_Report;
""")

results = cursor.fetchall()

for row in results:
    print(row)

connection.close()

This Python script connects to the SQLite database, retrieves information from the "Sales_Report" view, displays the results, and closes the database connection.

8. Database Screenshots

The database tables and "Sales_Report" view were inspected using DB Browser for SQLite.

Sales Report

The "Sales_Report" view displays the combined product and order information together with the calculated sales value.

Add the screenshot of the Sales_Report table here.

9. Conclusion

This project demonstrates the fundamental concepts of relational database design and SQL. The database uses multiple related tables, primary keys, foreign keys, normalization principles, JOIN queries, sales calculations, and an automated inventory report.

Python integration was also demonstrated to show how an application can connect to and retrieve information from an SQLite database.
