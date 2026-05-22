"""
API endpoints for the application
"""

from flask import Flask, jsonify, request
from models import Order, OrderOffer, OrderPricing, OrderTax
from services import OrderService, OrderOfferService

app = Flask(__name__)

order_service = OrderService()
order_offer_service = OrderOfferService()

@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id: int):
    """
    Retrieves an order by ID

    Args:
        id (int): The order ID

    Returns:
        jsonify: The order object as JSON
    """
    order = order_service.get_order(id)
    return jsonify(order.__dict__)

@app.route('/orders/<int:id>/pricing', methods=['GET'])
def get_pricing(id: int):
    """
    Retrieves the pricing for an order

    Args:
        id (int): The order ID

    Returns:
        jsonify: The pricing object as JSON
    """
    order = order_service.get_order(id)
    pricing = order_service.calculate_pricing(order)
    return jsonify(pricing.__dict__)

@app.route('/orders/<int:id>/taxes', methods=['GET'])
def get_taxes(id: int):
    """
    Retrieves the taxes for an order

    Args:
        id (int): The order ID

    Returns:
        jsonify: The tax object as JSON
    """
    order = order_service.get_order(id)
    taxes = order_service.calculate_taxes(order)
    return jsonify(taxes.__dict__)

@app.route('/offers/<int:id>', methods=['GET'])
def get_offer(id: int):
    """
    Retrieves an offer by ID

    Args:
        id (int): The offer ID

    Returns:
        jsonify: The offer object as JSON
    """
    offer = order_offer_service.get_offer(id)
    return jsonify(offer.__dict__)