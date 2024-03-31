import factory
from factory.alchemy import SQLAlchemyModelFactory

from app import models
from config.settings import db


class ProductFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.Products
        sqlalchemy_session = db
        sqlalchemy_session_persistence = "commit"

    product_code = factory.Sequence(lambda n: f"code{n}")
    name = factory.Faker("name")
    unit_price = factory.Faker("random_int", min=100, max=1000)
    percent_tax = factory.Faker("random_int", min=1, max=10)
