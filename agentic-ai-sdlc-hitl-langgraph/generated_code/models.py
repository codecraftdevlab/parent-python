"""
Data models for the project.
"""

class Order:
    """
    Order model.
    """

    def __init__(self, id, customer_id, order_date):
        """
        Initialize the order.
        
        Args:
            id (int): The order ID.
            customer_id (int): The customer ID.
            order_date (str): The order date.
        """
        self.id = id
        self.customer_id = customer_id
        self.order_date = order_date

    def __str__(self):
        """
        Get the string representation of the order.
        
        Returns:
            str: The string representation of the order.
        """
        return f"Order {self.id} for customer {self.customer_id} on {self.order_date}"

class OrderOffer:
    """
    Order offer model.
    """

    def __init__(self, id, order_id, offer_date):
        """
        Initialize the order offer.
        
        Args:
            id (int): The order offer ID.
            order_id (int): The order ID.
            offer_date (str): The offer date.
        """
        self.id = id
        self.order_id = order_id
        self.offer_date = offer_date

    def __str__(self):
        """
        Get the string representation of the order offer.
        
        Returns:
            str: The string representation of the order offer.
        """
        return f"Order offer {self.id} for order {self.order_id} on {self.offer_date}"

class OrderPricing:
    """
    Order pricing model.
    """

    def __init__(self, id, order_id, price):
        """
        Initialize the order pricing.
        
        Args:
            id (int): The order pricing ID.
            order_id (int): The order ID.
            price (float): The price.
        """
        self.id = id
        self.order_id = order_id
        self.price = price

    def __str__(self):
        """
        Get the string representation of the order pricing.
        
        Returns:
            str: The string representation of the order pricing.
        """
        return f"Order pricing {self.id} for order {self.order_id} with price {self.price}"

class OrderTaxes:
    """
    Order taxes model.
    """

    def __init__(self, id, order_id, tax_amount):
        """
        Initialize the order taxes.
        
        Args:
            id (int): The order taxes ID.
            order_id (int): The order ID.
            tax_amount (float): The tax amount.
        """
        self.id = id
        self.order_id = order_id
        self.tax_amount = tax_amount

    def __str__(self):
        """
        Get the string representation of the order taxes.
        
        Returns:
            str: The string representation of the order taxes.
        """
        return f"Order taxes {self.id} for order {self.order_id} with tax amount {self.tax_amount}"