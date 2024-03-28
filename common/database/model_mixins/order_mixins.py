from datetime import datetime

from pytz import timezone  # type: ignore
from sqlalchemy import BigInteger, Column, DateTime, String, Integer
from sqlalchemy.orm import declarative_mixin

from config.settings import TIME_ZONE

def current_timestamp():
    jst = timezone(TIME_ZONE)
    return datetime.now(jst)

@declarative_mixin
class OrderMixin:
    code = Column(String(255), unique=True, nullable=False)
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