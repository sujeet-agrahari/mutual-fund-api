from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    userId = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    username = Column(String, nullable=False)
    full_name = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(userId={self.userId}, email={self.email})>"