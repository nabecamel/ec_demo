from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Column, DateTime, String, text
from sqlalchemy.orm import Mapped, declarative_mixin, declared_attr, relationship

if TYPE_CHECKING:
    from app.models.orders import Order


@declarative_mixin
class UserMixin:
    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, comment="名前")
    email = Column(String(255), nullable=False, unique=True, comment="メールアドレス")
    password = Column(String(255), nullable=False, comment="パスワード")
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

    @declared_attr
    def orders(cls) -> Mapped["Order"]:
        return relationship("Order", backref="user")
