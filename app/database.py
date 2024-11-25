from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Usar la URL externa proporcionada por Render
DATABASE_URL = "postgresql://tanamix22:Agl6eavXkd1cAsXxHu7GmgjMRawHatvd@dpg-ct24gb0gph6c73bmr6kg-a.oregon-postgres.render.com/esmeraldadb_ypiv"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()