from sqlalchemy import Column, String
from models.base_model import Base
import enum

class Admin(Base):
    __tablename__ = "admins"

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole))