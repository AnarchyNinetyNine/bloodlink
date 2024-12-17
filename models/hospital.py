from sqlalchemy import Column, String, JSON, Enum
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from models.role import UserRole
import enum

class Hospital(BaseModel, Base):
    __tablename__ = "hospitals"

    name = Column(String(255), nullable=False)
    location = Column(JSON, nullable=True)
    cmd = Column(String(255), nullable=False)
    contact_info = Column(JSON, nullable=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False)

    blood_requests = relationship("BloodRequest", back_populates="requester")

