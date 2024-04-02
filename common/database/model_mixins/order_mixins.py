from datetime import datetime

from pytz import timezone  # type: ignore
from sqlalchemy import BigInteger, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_mixin

from config.settings import TIME_ZONE

def current_timestamp():
    jst = timezone(TIME_ZONE)
    return datetime.now(jst)

@declarative_mixin
class OrderMixin:
    id = Column(BigInteger, primary_key=True)
    code = Column(String(255), unique=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.id"),nullable = False)
    post_code = Column(String(10), nullable=False)
    user_address1 = Column(String(255), nullable=False)
    user_address2 = Column(String(255), nullable=False)
    user_tel = Column(String(15), nullable=False)
    user_email = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False)
    shipping_post_code = Column(String(10), nullable=False)
    shipping_user_address1 = Column(String(255), nullable=False)
    shipping_user_address2 = Column(String(255), nullable=False)
    shipping_user_tel = Column(String(15), nullable=False)
    shipping_user_email = Column(String(255), nullable=False)
    shipping_user_name = Column(String(255), nullable=False)
    tax = Column(Integer, nullable=False)
    subtotal = Column(Integer, nullable=False)
    total_price = Column(Integer, nullable=False)
    payment_dated_at = Column(DateTime)
    created_at = Column(DateTime, nullable=False, default=current_timestamp)
    updated_at = Column(
        DateTime, nullable=False, default=current_timestamp, onupdate=current_timestamp
        )


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
    