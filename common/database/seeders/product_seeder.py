from app import models
from common.database import factories


class ProductSeeder:
    factories.ProductFactory.create(
        product_code="code1",
        name="product1",
        unit_price=100,
        percent_tax=5
    )
