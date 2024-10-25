from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://tanamix22:PafBFaytY80Gm6ACraqOsZHlSIXdRo8C@dpg-cse0tum8ii6s73b19a20-a:5432/esmeraldadb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()