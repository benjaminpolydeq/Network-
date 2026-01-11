from sqlalchemy.orm import Session
from . import models

def create_contact(db: Session, contact_data: dict):
    contact = models.Contact(**contact_data)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

def get_contacts(db: Session):
    return db.query(models.Contact).all()

def update_contact_importance(db: Session, contact_id: int, importance: int):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if contact:
        contact.importance = importance
        db.commit()
        db.refresh(contact)
    return contact
