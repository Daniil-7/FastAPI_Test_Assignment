from .users import users
from .products import products
from .categories import categories
from .base import metadata, engine

metadata.create_all(bind=engine)
