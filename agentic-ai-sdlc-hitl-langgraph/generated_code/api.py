"""
API endpoints for the application.

This file contains functions that handle API requests and return responses.
"""

from fastapi import FastAPI, HTTPException
from .services import OrderService, CustomerService, ProductService
from .models import Order, Customer, Product
from .config import API_HOST, API_PORT

app = FastAPI()

order_service = OrderService()
customer_service = CustomerService()
product_service = ProductService()

@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    """
    Retrieves an order by ID.

    Args:
        order_id (int): The order ID.

    Returns:
        Order: The order with the specified ID.
    """
    order = order_service.get_order(order_id)
    if order:
        return order.to_dict()
    else:
        raise HTTPException(status_code=404, detail="Order not found")

@app.post("/orders")
async def create_order(customer_id: int, product_id: int, price: float):
    """
    Creates a new order.

    Args:
        customer_id (int): The customer ID.
        product_id (int): The product ID.
        price (float): The order price.

    Returns:
        Order: The newly created order.
    """
    order = order_service.create_order(customer_id, product_id, price)
    return order.to_dict()

@app.get("/customers/{customer_id}")
async def get_customer(customer_id: int):
    """
    Retrieves a customer by ID.

    Args:
        customer_id (int): The customer ID.

    Returns:
        Customer: The customer with the specified ID.
    """
    customer = customer_service.get_customer(customer_id)
    if customer:
        return customer.to_dict()
    else:
        raise HTTPException(status_code=404, detail="Customer not found")

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    """
    Retrieves a product by ID.

    Args:
        product_id (int): The product ID.

    Returns:
        Product: The product with the specified ID.
    """
    product = product_service.get_product(product_id)
    if product:
        return product.to_dict()
    else:
        raise HTTPException(status_code=404, detail="Product not found")