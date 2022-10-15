import sqlalchemy
from .base import metadata
import datetime

categories = sqlalchemy.Table(
    "categories", 
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("image", sqlalchemy.String),
    sqlalchemy.Column("created", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated", sqlalchemy.DateTime, default=datetime.datetime.utcnow)
)