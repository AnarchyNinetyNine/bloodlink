from sqlalchemy import Column, String, Enum, UniqueConstraint
from models.base_model import Base
from models.donor import BloodType

class BloodCompatibility(Base):
    __tablename__ = "blood_compatibility"

    donor_type = Column(Enum(BloodType), nullable=False)
    recipient_type = Column(Enum(BloodType), nullable=False)

    __table_args__ = (UniqueConstraint("donor_type", "recipient_type"),)
