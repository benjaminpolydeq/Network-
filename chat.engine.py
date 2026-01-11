def add_message(db, contact_id, content):
    from models.message import Message
    msg = Message(contact_id=contact_id, content=content)
    db.add(msg)
    db.commit()
    return msg