from sqlalchemy import Column, VARCHAR, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relation

from .base import BaseModel
from .cities import DBCity


class DBUser(BaseModel):
    __tablename__ = 'users'

    email = Column(VARCHAR(100), nullable=True)
    password = Column(VARCHAR(100), nullable=True)
    first_name = Column(VARCHAR(255), nullable=True)
    last_name = Column(VARCHAR(255), nullable=True)
    is_seller = Column(Boolean, nullable=True)
    phone = Column(VARCHAR(50), nullable=True)
    zip_code = Column(VARCHAR(50), nullable=True)
    city_id = Column(Integer, ForeignKey('cities.id', ondelete='CASCADE'), nullable=True, index=True)
    street = Column(VARCHAR(100), nullable=True)
    home = Column(VARCHAR(100), nullable=True)


class DBUserWithCity(DBUser):
    city = relation(DBCity)
