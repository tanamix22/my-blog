from sqlalchemy.orm import Session
from ..models.homepage_models import HomePageImage
from ..schemas.homepage_schemas import HomePageImageCreate, HomePageImageUpdate

def get_images(db: Session, skip: int = 0, limit: int = 10):
    return db.query(HomePageImage).offset(skip).limit(limit).all()

def create_image(db: Session, image: HomePageImageCreate):
    db_image = HomePageImage(**image.dict())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

def get_image(db: Session, image_id: int):
    return db.query(HomePageImage).filter(HomePageImage.id == image_id).first()

def delete_image(db: Session, image_id: int):
    db_image = get_image(db, image_id)
    if db_image:
        db.delete(db_image)
        db.commit()
    return db_image

def update_image(db: Session, image_id: int, image: HomePageImageUpdate):
    db_image = get_image(db, image_id)
    if db_image:
        for key, value in image.dict().items():
            setattr(db_image, key, value)
        db.commit()
        db.refresh(db_image)
    return db_image