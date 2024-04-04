from sqlalchemy import Column, Integer, String
from database import Base

# Define a User model. This is essentially creating a table structure as a Python class.
# It's like drawing a blueprint before building something cool.
class User(Base):
    __tablename__ = "users"  # The table name in the database
    
    # Here are the columns. Think of them as the rooms in your data castle.
    id = Column(Integer, primary_key=True, index=True)  # Every castle needs a unique identifier!
    username = Column(String, index=True)  # A name for each inhabitant
    email = Column(String, index=True)  # Their carrier pigeon address
    age = Column(Integer)  # How many winters they've seen
