from fastapi import FastAPI
from services import OrderService, PricingService, TaxesFeesService
from models import Order, Pricing, TaxesFees
from config import Config

app = FastAPI()

config = Config()
order_service = OrderService(config)
pricing_service = PricingService(config)
taxes_fees_service = TaxesFeesService(config)

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    """
    Returns the order information for the given order ID.
    :param order_id: int
    :return: Order
    """
    # Order logic here
    return Order(order_id, 100.0, 10.0, 5.0)

@app.get("/pricing/{order_id}")
def get_pricing(order_id: int):
    """
    Returns the pricing information for the given order ID.
    :param order_id: int
    :return: Pricing
    """
    return pricing_service.get_pricing(order_id)

@app.get("/taxes-fees/{order_id}")
def get_taxes_fees(order_id: int):
    """
    Returns the taxes and fees information for the given order ID.
    :param order_id: int
    :return: TaxesFees
    """
    return taxes_fees_service.get_taxes_fees(order_id)