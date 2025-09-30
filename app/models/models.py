from enum import Enum

from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.fields.base import RESTRICT, SET_NULL, CASCADE


class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"


class BasicModel(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)

    class Meta:
        abstract = True


class User(BasicModel):
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    role = fields.CharEnumField(UserRole, default=UserRole.USER)

    class Meta:
        table = "user"


class Nationality(BasicModel):
    name = fields.CharField(max_length=50)

    productions: fields.ReverseRelation["Production"]

    class Meta:
        table = "nationality"


class Genre(BasicModel):
    name = fields.CharField(max_length=50)

    productions: fields.ReverseRelation["Production"]

    class Meta:
        table = "genre"


class ProductionCategory(BasicModel):
    name = fields.CharField(max_length=50)

    productions: fields.ReverseRelation["Production"]

    class Meta:
        table = "production_category"


class Production(BasicModel):
    year = fields.IntField()
    title = fields.CharField(max_length=255)
    director = fields.CharField(max_length=100)
    studio = fields.CharField(max_length=100)

    nationality: fields.ForeignKeyRelation["Nationality"] = fields.ForeignKeyField(
        "models.Nationality", related_name="productions", on_delete=CASCADE
    )
    genre: fields.ForeignKeyRelation["Genre"] = fields.ForeignKeyField(
        "models.Genre", related_name="productions", on_delete=CASCADE
    )
    category: fields.ForeignKeyRelation["ProductionCategory"] = fields.ForeignKeyField(
        "models.ProductionCategory", related_name="productions", on_delete=CASCADE
    )

    products: fields.ReverseRelation["Product"]

    class Meta:
        table = "production"


class ProductCategory(BasicModel):
    name = fields.CharField(max_length=50)

    products: fields.ReverseRelation["Product"]

    class Meta:
        table = "product_category"


class Product(BasicModel):
    description = fields.CharField(max_length=255)

    category: fields.ForeignKeyRelation["ProductCategory"] = fields.ForeignKeyField(
        "models.ProductCategory", related_name="products", on_delete=CASCADE
    )
    production: fields.ForeignKeyRelation[Production] = fields.ForeignKeyField(
        "models.Production", related_name="products", on_delete=CASCADE
    )

    class Meta:
        table = "product"


class Site(BasicModel):
    name = fields.CharField(max_length=100)
    link = fields.CharField(max_length=255)

    class Meta:
        table = "site"


class Favorite(Model):
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", "favorite", on_delete=CASCADE
    )
    product: fields.ForeignKeyRelation[Product] = fields.ForeignKeyField(
        "models.Product", related_name="favorites", on_delete=CASCADE
    )

    class Meta:
        table = "favorite"
        unique_together = ("user", "product")


class ProductSite(Model):
    product: fields.ForeignKeyRelation[Product] = fields.ForeignKeyField(
        "models.Product", related_name="products_site", on_delete=CASCADE
    )
    site: fields.ForeignKeyRelation[Site] = fields.ForeignKeyField(
        "models.Site", related_name="products_site", on_delete=CASCADE
    )

    class Meta:
        table = "product_site"
        unique_together = ("product", "site")


User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)

Nationality_Pydantic = pydantic_model_creator(Nationality, name="Nationality")
NationalityIn_Pydantic = pydantic_model_creator(Nationality, name="NationalityIn", exclude_readonly=True)

Genre_Pydantic = pydantic_model_creator(Genre, name="Genre")
ProductionCategory_Pydantic = pydantic_model_creator(ProductionCategory, name="ProductionCategory")

Production_Pydantic = pydantic_model_creator(Production, name="Production")
ProductCategory_Pydantic = pydantic_model_creator(ProductCategory, name="ProductCategory")
Product_Pydantic = pydantic_model_creator(Product, name="Product")
Site_Pydantic = pydantic_model_creator(Site, name="Site")

Favorite_Pydantic = pydantic_model_creator(Favorite, name="Favorite")
ProductSite_Pydantic = pydantic_model_creator(ProductSite, name="ProductSite")
