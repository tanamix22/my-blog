from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class HomePageImage(Base):
    __tablename__ = "homepage_images"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, index=True)
    description = Column(String, index=True)