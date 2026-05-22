"""
Business logic for the application.

This file contains classes and functions that encapsulate the business logic of the application.
"""

from .models import Order, Customer, Product
from .config import DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD, DB_NAME
import mysql.connector

class OrderService:
    """
    Provides methods for working with orders.

    Attributes:
        db_connection (mysql.connector.connection.MySQLConnection): The database connection.
    """

    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            database=DB_NAME
        )

    def get_order(self, order_id: int) -> Order:
        """
        Retrieves an order by ID.

        Args:
            order_id (int): The order ID.

        Returns:
            Order: The order with the specified ID.
        """
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
        row = cursor.fetchone()
        if row:
            return Order(row[0], row[1], row[2], row[3])
        else:
            return None

    def create_order(self, customer_id: int, product_id: int, price: float) -> Order:
        """
        Creates a new order.

        Args:
            customer_id (int): The customer ID.
            product_id (int): The product ID.
            price (float): The order price.

        Returns:
            Order: The newly created order.
        """
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO orders (customer_id, product_id, price) VALUES (%s, %s, %s)", (customer_id, product_id, price))
        self.db_connection.commit()
        return Order(cursor.lastrowid, customer_id, product_id, price)

class CustomerService:
    """
    Provides methods for working with customers.

    Attributes:
        db_connection (mysql.connector.connection.MySQLConnection): The database connection.
    """

    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            database=DB_NAME
        )

    def get_customer(self, customer_id: int) -> Customer:
        """
        Retrieves a customer by ID.

        Args:
            customer_id (int): The customer ID.

        Returns:
            Customer: The customer with the specified ID.
        """
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
        row = cursor.fetchone()
        if row:
            return Customer(row[0], row[1])
        else:
            return None

class ProductService:
    """
    Provides methods for working with products.

    Attributes:
        db_connection (mysql.connector.connection.MySQLConnection): The database connection.
    """

    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            database=DB_NAME
        )

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product by ID.

        Args:
            product_id (int): The product ID.

        Returns:
            Product: The product with the specified ID.
        """
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        row = cursor.fetchone()
        if row:
            return Product(row[0], row[1])
        else:
            return None