from datetime import datetime
from typing import TYPE_CHECKING

from pytz import timezone  # type: ignore
from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.orm import Mapped, declarative_mixin, declared_attr, relationship

from config.settings import TIME_ZONE


def current_timestamp():
    jst = timezone(TIME_ZONE)
    return datetime.now(jst)


if TYPE_CHECKING:
    from app.models.orders import Order


@declarative_mixin
class UserMixin:
    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, comment="名前")
    email = Column(String(255), nullable=False, unique=True, comment="メールアドレス")
    password = Column(String(255), nullable=False, comment="パスワード")
    created_at = Column(
        DateTime, nullable=False, default=current_timestamp, comment="作成日時"
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=current_timestamp,
        onupdate=current_timestamp,
        comment="更新日時",
    )

    @declared_attr
    def orders(cls) -> Mapped["Order"]:
        return relationship("Order", backref="user")
