from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel

class BloodDonation(BaseModel, Base):
    __tablename__ = "blood_donations"

    donor_id = Column(String(36), ForeignKey("donors.id", ondelete="CASCADE"), nullable=False)
    request_id = Column(String(36), ForeignKey("blood_requests.id", ondelete="CASCADE"), nullable=False)
    donated_quantity = Column(Integer, nullable=False)

    donor = relationship("Donor", back_populates="donations")
    request = relationship("BloodRequest", back_populates="donations")
