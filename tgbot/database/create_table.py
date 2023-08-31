from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, VARCHAR, INTEGER

BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger, unique=True, nullable=False, primary_key=True)

    user_name = Column(VARCHAR(32), unique=True, nullable=True)

    name = Column(VARCHAR(20), unique=False, nullable=True)

    city = Column(VARCHAR(20), unique=False, nullable=True)

    vacancies = Column(VARCHAR(30), unique=False, nullable=True)

    employment = Column(VARCHAR(20), unique=False, nullable=True)

    schedule = Column(VARCHAR(20), unique=False, nullable=True)

    status = Column(VARCHAR())

    access = Column(INTEGER, unique=False, default=0)
