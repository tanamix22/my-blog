from fastapi import APIRouter, HTTPException
from ..models import models
from ..schemas import schemas
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..crud import homepage_crud
from ..models.homepage_models import HomePageImage
from ..schemas.homepage_schemas import HomePageImage as HomePageImageSchema, HomePageImageCreate, HomePageImageUpdate
from ..database import SessionLocal, engine
from ..auth.jwt_bearer import JWTBearer

HomePageImage.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/homepage/images/", response_model=HomePageImageSchema, dependencies=[Depends(JWTBearer())])
def create_image(
    image: HomePageImageCreate,
    db: Session = Depends(get_db)
):
    return homepage_crud.create_image(db=db, image=image)

@router.get("/homepage/images/", response_model=List[HomePageImageSchema])
def read_images(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    images = homepage_crud.get_images(db, skip=skip, limit=limit)
    return images

@router.get("/homepage/images/{image_id}", response_model=HomePageImageSchema, dependencies=[Depends(JWTBearer())])
def read_image(image_id: int, db: Session = Depends(get_db)):
    db_image = homepage_crud.get_image(db, image_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image

@router.delete("/homepage/images/{image_id}", response_model=HomePageImageSchema, dependencies=[Depends(JWTBearer())])
def delete_image(image_id: int, db: Session = Depends(get_db)):
    db_image = homepage_crud.delete_image(db, image_id=image_id)
    return db_image

@router.put("/homepage/images/{image_id}", response_model=HomePageImageSchema, dependencies=[Depends(JWTBearer())])
def update_image(
    image_id: int,
    image: HomePageImageUpdate,
    db: Session = Depends(get_db)
):
    db_image = homepage_crud.update_image(db, image_id=image_id, image=image)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image