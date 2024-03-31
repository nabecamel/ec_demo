from common.database.model_mixins.order_mixins import ProductMixin
from config.settings import Base


class Order(Base, ProductMixin):
    __tablename__ = "products"
    