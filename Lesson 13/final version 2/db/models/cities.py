from sqlalchemy import Column, VARCHAR, Boolean, Integer, ForeignKey
from .base import BaseModel


class DBCity(BaseModel):
    __tablename__ = 'cities'

    name = Column(VARCHAR(100), nullable=False)
