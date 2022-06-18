from db import Base, engine
from .user import User
from .group import Group
from .join import Join
from .reviews import Review
from .category import Category

__all__ = [
    "User",
    "Group",
    "Join",
    "Review",
    "Category",
]

Base.metadata.create_all(engine)
