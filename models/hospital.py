from sqlalchemy import Column, String, JSON
from sqlalchemy.orm import relationship
from models.base_model import Base
import enum

class UserRole(enum.Enum):
    DONOR = "DONOR"
    HOSPITAL = "HOSPITAL"
    ADMIN = "ADMIN"

class UserRole(enum.Enum):
    DONOR = "DONOR"
    HOSPITAL = "HOSPITAL"
    ADMIN = "ADMIN"

class Hospital(Base):
    __tablename__ = "hospitals"

    name = Column(String(255), nullable=False)
    location = Column(JSON)
    cmd = Column(String(255), nullable=False)
    contact_info = Column(JSON)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole))
    

    blood_requests = relationship("BloodRequest", back_populates="requester")
