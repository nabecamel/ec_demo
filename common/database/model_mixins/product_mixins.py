from datetime import datetime

from pytz import timezone  # type: ignore
from sqlalchemy import BigInteger, Column, DateTime, String, text
from sqlalchemy.orm import declarative_mixin

from config.settings import TIME_ZONE


def current_timestamp():
    jst = timezone(TIME_ZONE)
    return datetime.now(jst)


@declarative_mixin
class ProductMixin:
    id = Column(BigInteger, primary_key=True)
    code = Column(String(255), nullable=False, unique=True, comment="商品コード")
    name = Column(String(255), nullable=False, comment="商品名")
    unit_price = Column(BigInteger, nullable=False, comment="単価")
    percent_tax = Column(String(255), nullable=False, comment="消費税率")
    created_at = Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="作成日時",
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        comment="更新日時",
    )
