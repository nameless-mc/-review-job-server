from db import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, BigInteger


class Review(Base):
    __tablename__ = 'reviews'
    id = Column('id', BigInteger, primary_key=True, index=True)
    user_id = Column('user_id', BigInteger, ForeignKey(
        'users.id', onupdate='CASCADE', ondelete='CASCADE'), index=True)
    group_id = Column('group_id', BigInteger, ForeignKey(
        "groups.id", onupdate='CASCADE', ondelete='CASCADE'),  index=True)
    name = Column('name', String, nullable=False, index=True)
    note = Column('note', String(1000), nullable=False, index=True)
    category_id = Column("category_id", BigInteger, ForeignKey(
        "categories.id", onupdate='CASCADE', ondelete='CASCADE'), nullable=False, index=True)
