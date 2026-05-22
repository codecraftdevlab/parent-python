from api import app
from services import OrderService
from config import Config

config = Config()
order_service = OrderService(config)

def main():
    order_service.upgrade_to_spring_boot_4()
    order_service.ensure_pricing_service_compatibility()
    order_service.test_taxes_fees_service()
    app.run()

if __name__ == "__main__":
    main()