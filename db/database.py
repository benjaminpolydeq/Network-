from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

engine = create_engine(
    "sqlite:///network.db",
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

def init_db():
    from .models import Contact
    Base.metadata.create_all(bind=engine)