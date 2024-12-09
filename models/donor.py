from sqlalchemy import Column, String, Enum, ForeignKey, DateTime, Boolean, JSON
from sqlalchemy.orm import relationship
from models.base_model import Base
import enum

class Gender(enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class BloodType(enum.Enum):
    O_POS = "O+"
    O_NEG = "O-"
    A_POS = "A+"
    A_NEG = "A-"
    B_POS = "B+"
    B_NEG = "B-"
    AB_POS = "AB+"
    AB_NEG = "AB-"

class Donor(Base):
    __tablename__ = "donors"

    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    gender = Column(Enum(Gender))
    blood_type = Column(Enum(BloodType))
    address = Column(String(255))
    location = Column(JSON)
    last_donation_date = Column(DateTime)
    availability = Column(Boolean)

    donations = relationship("BloodDonation", back_populates="donor")
    confirmations = relationship("BloodRequestConfirmation", back_populates="donor")
    user = relationship("User", back_populates="donor")
