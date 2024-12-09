from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship
from models.base_model import Base
import enum

class UserRole(enum.Enum):
    DONOR = "DONOR"
    HOSPITAL = "HOSPITAL"
    ADMIN = "ADMIN"

class User(Base):
    __tablename__ = "users"

    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole))
    phone_number = Column(String(255), unique=True, nullable=False)

    donor = relationship("Donor", back_populates="user", uselist=False)
    hospital = relationship("Hospital", back_populates="user", uselist=False)
    admin = relationship("Admin", back_populates="user", uselist=False)
