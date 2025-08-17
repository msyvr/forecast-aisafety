from dotenv import load_dotenv

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg2:://username:password@localhost:5432/ai_forecasting_db')

if DATABASE_URL.startswith('postgresql'):
    engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)
else:
    engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    """Create all database tables"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("All tables created.")

def get_db_session():
    """Get database session"""
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

def get_db():
    """Generator for database sessions (for dependency injection)"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()