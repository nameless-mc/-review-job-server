from db import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String, BigInteger


class Group(Base):
    __tablename__ = 'groups'
    id = Column('id', BigInteger, primary_key=True, index=True)
    name = Column('name', String, nullable=False)
    code = Column('code', String, nullable=False)
