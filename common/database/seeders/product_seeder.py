from app import models
from common.database import factories


class ProductSeeder:
    def handle(self):
        # 製品データの例
        # factories.ProductFactory.create_batch(20)  # ２0個の製品データを作成
        factories.ProductFactory.create(
            code="code1", name="product1", unit_price=100, percent_tax=5
        )
