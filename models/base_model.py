from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func

@as_declarative()
class Base:
    """Base class for all models."""
    id = Column(String(36), primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
