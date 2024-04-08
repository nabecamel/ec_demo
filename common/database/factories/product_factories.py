from uuid import uuid4

import factory
from factory.alchemy import SQLAlchemyModelFactory

from app import models
from config.settings import db


class ProductFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.Product
        sqlalchemy_session = db
        sqlalchemy_session_persistence = "commit"

    code = factory.LazyFunction(uuid4)
    name = factory.Faker("name")
    unit_price = factory.Faker("random_int", min=100, max=1000)
    percent_tax = factory.Faker("random_int", min=1, max=10)
