import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is not set.")