from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)
    domain = Column(String)
    occasion = Column(String)
    topics = Column(Text)
    next_action = Column(Text)
    importance = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)