from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DATABASE_URL

# Create an engine. This is the core interface to the database. 
# It's how SQLAlchemy speaks to your database using your DB's language.
engine = create_engine(DATABASE_URL)

# Here we configure a session factory. Think of sessions as your personal convoy into the database.
# They carry your queries to the database and bring back the answers.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models. It's like the foundation of a house where all models will live.
Base = declarative_base()
