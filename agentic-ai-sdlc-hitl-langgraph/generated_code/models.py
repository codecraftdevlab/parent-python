"""
Data models for the application.

This file contains classes representing the data structures used in the application.
"""

from typing import Dict

class Order:
    """
    Represents an order.

    Attributes:
        id (int): The order ID.
        customer_id (int): The customer ID.
        product_id (int): The product ID.
        price (float): The order price.
    """

    def __init__(self, id: int, customer_id: int, product_id: int, price: float):
        self.id = id
        self.customer_id = customer_id
        self.product_id = product_id
        self.price = price

    def to_dict(self) -> Dict:
        """
        Returns a dictionary representation of the order.

        Returns:
            Dict: A dictionary containing the order's attributes.
        """
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'product_id': self.product_id,
            'price': self.price
        }

class Customer:
    """
    Represents a customer.

    Attributes:
        id (int): The customer ID.
        name (str): The customer name.
    """

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def to_dict(self) -> Dict:
        """
        Returns a dictionary representation of the customer.

        Returns:
            Dict: A dictionary containing the customer's attributes.
        """
        return {
            'id': self.id,
            'name': self.name
        }

class Product:
    """
    Represents a product.

    Attributes:
        id (int): The product ID.
        name (str): The product name.
    """

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def to_dict(self) -> Dict:
        """
        Returns a dictionary representation of the product.

        Returns:
            Dict: A dictionary containing the product's attributes.
        """
        return {
            'id': self.id,
            'name': self.name
        }