from common.database.model_mixins.order_mixins import OrderDetailMixin, OrderMixin
from config.settings import Base


class Order(Base, OrderMixin):
    __tablename__ = "orders"
class OrderDetail(Base, OrderDetailMixin):
    __tablename__ = "order_details"