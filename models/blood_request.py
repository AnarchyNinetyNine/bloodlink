from sqlalchemy import Column, String, Enum, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from models.donor import BloodType

class BloodRequest(BaseModel, Base):
    __tablename__ = "blood_requests"

    requester_id = Column(String(36), ForeignKey("hospitals.id", ondelete="CASCADE"), nullable=False)
    blood_type = Column(Enum(BloodType), nullable=False)
    quantity = Column(Integer, nullable=False)
    urgency = Column(Boolean, nullable=False)
    status = Column(String(255), nullable=False)
    time_frame = Column(DateTime, nullable=False)

    donations = relationship("BloodDonation", back_populates="request")
    confirmations = relationship("BloodRequestConfirmation", back_populates="blood_request")
    requester = relationship("Hospital", back_populates="blood_requests")
