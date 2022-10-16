import sqlalchemy
from .base import metadata
import datetime

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column(
        "id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True
    ),
    sqlalchemy.Column(
        "category_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("categories.id"),
        nullable=False,
    ),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("image", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Integer),
    sqlalchemy.Column("created", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
)
