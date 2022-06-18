from db import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String, BigInteger


class User(Base):
    __tablename__ = 'users'
    id = Column('id', BigInteger, primary_key=True, index=True)
    name = Column('name', String, nullable=False)
    signin_id = Column('signin_id', String, nullable=False)
    password = Column('pass', String, nullable=False)
