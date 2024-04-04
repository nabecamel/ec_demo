from common.database.model_mixins.product_mixins import ProductMixin
from config.settings import Base


class Product(Base, ProductMixin):
    __tablename__ = "products"
