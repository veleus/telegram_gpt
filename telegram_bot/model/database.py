from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_account = Column(String(255))
    role = Column(String(255), default='user')
    name = Column(String(255))

