from db import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, BigInteger


class Join(Base):
    __tablename__ = 'joins'
    user_id = Column('user_id', BigInteger, ForeignKey(
        'users.id', onupdate='CASCADE', ondelete='CASCADE'),  primary_key=True, index=True)
    group_id = Column('group_id', BigInteger, ForeignKey(
        "groups.id", onupdate='CASCADE', ondelete='CASCADE'), primary_key=True, index=True)
