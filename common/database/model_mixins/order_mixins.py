from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class OrderMixin:
    id = Column(BigInteger, primary_key=True)
    code = Column(String(255), unique=True, nullable=False, comment="注文コード")
    user_id = Column(
        BigInteger, ForeignKey("users.id"), nullable=False, comment="ユーザーID"
    )
    post_code = Column(String(10), nullable=False, comment="ユーザー郵便番号")
    user_address1 = Column(String(255), nullable=False, comment="ユーザー住所1")
    user_address2 = Column(String(255), nullable=False, comment="ユーザー住所2")
    user_tel = Column(String(15), nullable=False, comment="ユーザー電話番号")
    user_email = Column(String(255), nullable=False, comment="ユーザーメールアドレス")
    user_name = Column(String(255), nullable=False, comment="ユーザー名")
    shipping_post_code = Column(String(10), nullable=False, comment="配送先郵便番号")
    shipping_user_address1 = Column(
        String(255), nullable=False, comment="配送先ユーザー住所1"
    )
    shipping_user_address2 = Column(
        String(255), nullable=False, comment="配送先ユーザー住所2"
    )
    shipping_user_tel = Column(
        String(15), nullable=False, comment="配送先ユーザー電話番号"
    )
    shipping_user_email = Column(
        String(255), nullable=False, comment="配送先ユーザーメールアドレス"
    )
    shipping_user_name = Column(String(255), nullable=False, comment="配送先ユーザー名")
    tax = Column(Integer, nullable=False, comment="消費税")
    subtotal = Column(Integer, nullable=False, comment="小計")
    total_price = Column(Integer, nullable=False, comment="合計金額")
    payment_dated_at = Column(DateTime, comment="支払い日時")
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


@declarative_mixin
class OrderDetailMixin:
    id = Column(BigInteger, primary_key=True)
    order_id = Column(
        BigInteger, ForeignKey("orders.id"), nullable=False, comment="注文ID"
    )
    product_id = Column(
        BigInteger, ForeignKey("products.id"), nullable=False, comment="商品ID"
    )
    product_code = Column(String(255), nullable=False, comment="商品コード")
    product_name = Column(String(255), nullable=False, comment="商品名")
    product_unit_price = Column(BigInteger, nullable=False, comment="単価")
    product_percent_tax = Column(String(255), nullable=False, comment="税率")
    purchase_number = Column(BigInteger, nullable=False, comment="購入数")
    price = Column(BigInteger, nullable=False, comment="金額")
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
