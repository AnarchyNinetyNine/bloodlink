from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base

class Admin(Base):
    __tablename__ = "admins"

    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)

    user = relationship("User", back_populates="admin")
