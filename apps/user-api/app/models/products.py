from common.database.model_mixins.product_mixins import ProductMixin
from config.settings import Base


class Order(Base, ProductMixin):
    __tablename__ = "products"
