from sqlalchemy import Column, Integer, Text, DateTime, Boolean, ForeignKey
from datetime import datetime
from db import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"))
    discussion = Column(Text)
    summary = Column(Text)
    strategy = Column(Text)
    importance = Column(String)
    useful = Column(Boolean)
    date = Column(DateTime, default=datetime.utcnow)
    next_action = Column(Text)