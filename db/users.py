import sqlalchemy
from .base import metadata
import datetime

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, autoincrement=True, unique=True),
    sqlalchemy.Column("email", sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
    sqlalchemy.Column("is_superuser", sqlalchemy.Boolean),
    sqlalchemy.Column("created", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
)
