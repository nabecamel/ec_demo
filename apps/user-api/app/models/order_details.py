from common.database.model_mixins.order_details_mixin import OrderDetailMixin
from config.settings import Base


class Order(Base, OrderDetailMixin):
    __tablename__ = "order_details"
