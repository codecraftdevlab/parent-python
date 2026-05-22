"""
Data models for the application
"""

from typing import Dict

class Order:
    """
    Represents an order
    """
    def __init__(self, id: int, offers: Dict, pricing: Dict, taxes: Dict):
        """
        Initializes an Order object

        Args:
            id (int): The order ID
            offers (Dict): The order offers
            pricing (Dict): The order pricing
            taxes (Dict): The order taxes
        """
        self.id = id
        self.offers = offers
        self.pricing = pricing
        self.taxes = taxes

class OrderOffer:
    """
    Represents an order offer
    """
    def __init__(self, id: int, name: str, price: float):
        """
        Initializes an OrderOffer object

        Args:
            id (int): The offer ID
            name (str): The offer name
            price (float): The offer price
        """
        self.id = id
        self.name = name
        self.price = price

class OrderPricing:
    """
    Represents an order pricing
    """
    def __init__(self, id: int, base_price: float, discount: float):
        """
        Initializes an OrderPricing object

        Args:
            id (int): The pricing ID
            base_price (float): The base price
            discount (float): The discount
        """
        self.id = id
        self.base_price = base_price
        self.discount = discount

class OrderTax:
    """
    Represents an order tax
    """
    def __init__(self, id: int, tax_rate: float):
        """
        Initializes an OrderTax object

        Args:
            id (int): The tax ID
            tax_rate (float): The tax rate
        """
        self.id = id
        self.tax_rate = tax_rate