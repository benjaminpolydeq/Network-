from sqlalchemy import Column, Integer, String
from db import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    domain = Column(String)
    context = Column(String)