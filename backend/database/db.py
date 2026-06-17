from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:bhushanjadhav2007@localhost:5432/smart flow db"

engine = create_engine(DATABASE_URL)