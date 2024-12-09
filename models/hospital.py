from sqlalchemy import Column, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base

class Hospital(Base):
    __tablename__ = "hospitals"

    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    location = Column(JSON)
    cmd = Column(String(255), nullable=False)
    contact_info = Column(JSON)

    blood_requests = relationship("BloodRequest", back_populates="requester")
    user = relationship("User", back_populates="hospital")
