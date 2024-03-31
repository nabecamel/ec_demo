from datetime import datetime

from pytz import timezone  # type: ignore
from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.orm import declarative_mixin, declared_attr, relationship

from config.settings import TIME_ZONE


def current_timestamp():
    jst = timezone(TIME_ZONE)
    return datetime.now(jst)


@declarative_mixin
class ProductMixin:
    id = Column(BigInteger, primary_key=True)
    code = Column(String(255), nullable=False, unique=True, comment="商品コード")
    name = Column(String(255), comment="商品名")  # name って nullable=Falseにしなくていいのか気になります
    unit_price = Column(BigInteger, nullable=False, comment="単価")
    percent_tax = Column(String(255), nullable=False, comment="消費税率")
    created_at = Column(DateTime, nullable=False, default=current_timestamp)
    updated_at = Column(
        DateTime, nullable=False, default=current_timestamp, onupdate=current_timestamp
    )

    @declared_attr
    def orders(cls):
        return relationship("Order", backref="product")