from sqlalchemy.orm import Session
from .models import Contact

def create_contact(db: Session, data: dict):
    contact = Contact(**data)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

def get_contacts(db: Session):
    return db.query(Contact).order_by(Contact.created_at.desc()).all()