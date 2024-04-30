from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class AuthUser(BaseModel):
    __tablename__ = "auth_user"

    login = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    password = Column(String(32), nullable=False)
    age = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)