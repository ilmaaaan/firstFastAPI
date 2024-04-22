from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, JSON
from datetime import datetime, UTC
from sqlalchemy.orm import DeclarativeBase, relationship



class Base(DeclarativeBase):
    pass

class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable = False)
    username = Column(String, nullable = False)
    password = Column(String, nullable = False)
    registered_at = Column(TIMESTAMP, default = datetime.utcnow)
    role_id = Column(Integer, ForeignKey("roles.id"))

