from sqlalchemy import Column, String, Enum
from models.base_model import Base, BaseModel
from models.role import UserRole
import enum

class Admin(BaseModel, Base):
    __tablename__ = "admins"

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole))
