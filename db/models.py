from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from .database import Base

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)
    domain = Column(String)
    occasion = Column(String)
    topics = Column(Text)
    next_action = Column(Text)
    rendez_vous = Column(DateTime)
    importance = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now())
