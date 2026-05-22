class Order:
    """
    Represents an order.
    """

    def __init__(self, id, price, taxes, fees):
        self.id = id
        self.price = price
        self.taxes = taxes
        self.fees = fees

    def get_id(self):
        """
        Returns the order ID.
        :return: int
        """
        return self.id

    def get_price(self):
        """
        Returns the order price.
        :return: float
        """
        return self.price

    def get_taxes(self):
        """
        Returns the order taxes.
        :return: float
        """
        return self.taxes

    def get_fees(self):
        """
        Returns the order fees.
        :return: float
        """
        return self.fees


class Pricing:
    """
    Represents pricing information.
    """

    def __init__(self, id, price):
        self.id = id
        self.price = price

    def get_id(self):
        """
        Returns the pricing ID.
        :return: int
        """
        return self.id

    def get_price(self):
        """
        Returns the pricing information.
        :return: float
        """
        return self.price


class TaxesFees:
    """
    Represents taxes and fees information.
    """

    def __init__(self, id, taxes, fees):
        self.id = id
        self.taxes = taxes
        self.fees = fees

    def get_id(self):
        """
        Returns the taxes and fees ID.
        :return: int
        """
        return self.id

    def get_taxes(self):
        """
        Returns the taxes information.
        :return: float
        """
        return self.taxes

    def get_fees(self):
        """
        Returns the fees information.
        :return: float
        """
        return self.fees