from datetime import datetime

from pytz import timezone  # type: ignore
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String
from sqlalchemy.orm import declarative_mixin

from config.settings import TIME_ZONE


def current_timestamp():
    jst = timezone(TIME_ZONE)
    return datetime.now(jst)


@declarative_mixin
class OrderDetailMixin:
    id = Column(BigInteger, primary_key=True)
    order_id = Column(BigInteger, ForeignKey("orders.id"), nullable=False)
    product_id = Column(BigInteger, ForeignKey("products.id"), nullable=False)
    product_code = Column(String(255), nullable=False)
    product_name = Column(String(255), nullable=False)
    product_unit_price = Column(BigInteger, nullable=False)
    product_percent_tax = Column(String(255), nullable=False)
    purchase_number = Column(BigInteger, nullable=False)
    price = Column(BigInteger, nullable=False)
    created_at = Column(DateTime, nullable=False, default=current_timestamp)
    updated_at = Column(
        DateTime, nullable=False, default=current_timestamp, onupdate=current_timestamp
    )
