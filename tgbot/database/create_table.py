from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, VARCHAR, INTEGER

BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger, unique=True, nullable=False, primary_key=True)

    first_name = Column(VARCHAR(64), unique=False, nullable=False)

    user_name = Column(VARCHAR(32), unique=True, nullable=True)

    status = Column(INTEGER, unique=False, default=0)
