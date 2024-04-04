from dotenv import load_dotenv
import os

# Load environment variables from .env file if present
load_dotenv()

# Grabs the DATABASE_URL from the environment, make sure it's there or you'll be talking to ghosts.
DATABASE_URL = os.getenv("DATABASE_URL")
