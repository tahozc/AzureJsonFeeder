import json
from sqlalchemy.orm import Session
from models import User
from database import SessionLocal

def process_json(json_file):
    """This function is where JSON turns into database entries. Like magic, but with more typing."""
    with open(json_file, 'r') as file:
        data = json.load(file)  # Load the JSON data into a Python dictionary
        
        db = SessionLocal()  # Summon a session to talk to the database
        
        for user_data in data["users"]:  # Assuming our JSON has a 'users' key
            user = User(**user_data)  # Create a User instance for each
            db.add(user)  # Add each user to the session
            
        db.commit()  # Commit the session to save our changes to the database
        db.close()  # Always close your sessions, like closing the fridge door
