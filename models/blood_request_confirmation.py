from sqlalchemy import Column, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from models.base_model import Base

class BloodRequestConfirmation(Base):
    __tablename__ = "blood_request_confirmations"

    donor_id = Column(String(36), ForeignKey("donors.id", ondelete="CASCADE"), nullable=False)
    blood_request_id = Column(String(36), ForeignKey("blood_requests.id", ondelete="CASCADE"), nullable=False)
    confirmed_at = Column(DateTime)

    donor = relationship("Donor", back_populates="confirmations")
    blood_request = relationship("BloodRequest", back_populates="confirmations")

    __table_args__ = (UniqueConstraint("donor_id", "blood_request_id"),)
