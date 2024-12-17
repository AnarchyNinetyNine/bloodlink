from sqlalchemy import Column, String, Enum, DateTime, Boolean, JSON
from sqlalchemy.orm import relationship
from models.base_model import Base,  BaseModel
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

class UserRole(enum.Enum):
    DONOR = "DONOR"
    HOSPITAL = "HOSPITAL"
    ADMIN = "ADMIN"

class Donor(BaseModel, Base):
    __tablename__ = "donors"

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    gender = Column(Enum(Gender))
    blood_type = Column(Enum(BloodType))
    address = Column(String(255))
    location = Column(JSON)
    last_donation_date = Column(DateTime)
    availability = Column(Boolean)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole))
    phone_number = Column(String(255), unique=True, nullable=False)

    donations = relationship("BloodDonation", back_populates="donor")
    confirmations = relationship("BloodRequestConfirmation", back_populates="donor")
