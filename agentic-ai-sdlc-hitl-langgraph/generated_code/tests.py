"""
Tests for the application
"""

import unittest
from models import Order, OrderOffer, OrderPricing, OrderTax
from services import OrderService, OrderOfferService
from api import app

class TestOrderService(unittest.TestCase):
    """
    Tests for the OrderService
    """
    def test_get_order(self):
        """
        Tests retrieving an order
        """
        order_service = OrderService()
        order = order_service.get_order(1)
        self.assertIsInstance(order, Order)

    def test_calculate_pricing(self):
        """
        Tests calculating the pricing for an order
        """
        order_service = OrderService()
        order = Order(1, {}, {}, {})
        pricing = order_service.calculate_pricing(order)
        self.assertIsInstance(pricing, OrderPricing)

    def test_calculate_taxes(self):
        """
        Tests calculating the taxes for an order
        """
        order_service = OrderService()
        order = Order(1, {}, {}, {})
        taxes = order_service.calculate_taxes(order)
        self.assertIsInstance(taxes, OrderTax)

class TestOrderOfferService(unittest.TestCase):
    """
    Tests for the OrderOfferService
    """
    def test_get_offer(self):
        """
        Tests retrieving an offer
        """
        order_offer_service = OrderOfferService()
        offer = order_offer_service.get_offer(1)
        self.assertIsInstance(offer, OrderOffer)

class TestAPIEndpoints(unittest.TestCase):
    """
    Tests for the API endpoints
    """
    def test_get_order(self):
        """
        Tests retrieving an order
        """
        with app.test_client() as client:
            response = client.get('/orders/1')
            self.assertEqual(response.status_code, 200)

    def test_get_pricing(self):
        """
        Tests retrieving the pricing for an order
        """
        with app.test_client() as client:
            response = client.get('/orders/1/pricing')
            self.assertEqual(response.status_code, 200)

    def test_get_taxes(self):
        """
        Tests retrieving the taxes for an order
        """
        with app.test_client() as client:
            response = client.get('/orders/1/taxes')
            self.assertEqual(response.status_code, 200)

    def test_get_offer(self):
        """
        Tests retrieving an offer
        """
        with app.test_client() as client:
            response = client.get('/offers/1')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()