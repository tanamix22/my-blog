from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas
from ..database import SessionLocal, engine
import shutil
import os

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/blogs/", response_model=schemas.Blog)
def create_blog(
    title: str,
    content: str,
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Guardar la imagen en el sistema de archivos
    image_path = f"images/{image.filename}"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Crear la URL de la imagen
    image_url = f"/{image_path}"

    # Crear el blog en la base de datos
    blog_data = schemas.BlogCreate(title=title, content=content)
    return crud.create_blog(db=db, blog=blog_data, image_url=image_url)

@router.get("/blogs/", response_model=List[schemas.Blog])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db, skip=skip, limit=limit)
    return blogs

@router.get("/blogs/{blog_id}", response_model=schemas.Blog)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud.get_blog(db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog

@router.delete("/blogs/{blog_id}", response_model=schemas.Blog)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud.delete_blog(db, blog_id=blog_id)
    return db_blog