from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List

from ..crud import crud
from ..auth.jwt_bearer import JWTBearer

from ..models import models
from ..schemas import schemas
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

@router.post("/blogs/", response_model=schemas.Blog, dependencies=[Depends(JWTBearer())])
def create_blog(
    blog: schemas.BlogCreate,
    db: Session = Depends(get_db)
):
    return crud.create_blog(db=db, blog=blog)

@router.get("/blogs/", response_model=List[schemas.Blog])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db, skip=skip, limit=limit)
    return blogs

@router.get("/blogs/{blog_id}", response_model=schemas.Blog, dependencies=[Depends(JWTBearer())])
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud.get_blog(db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog

@router.delete("/blogs/{blog_id}", response_model=schemas.Blog, dependencies=[Depends(JWTBearer())])
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud.delete_blog(db, blog_id=blog_id)
    return db_blog

@router.put("/blogs/{blog_id}", response_model=schemas.Blog, dependencies=[Depends(JWTBearer())])
def update_blog(
    blog_id: int,
    blog: schemas.BlogUpdate,
    db: Session = Depends(get_db)
):
    db_blog = crud.update_blog(db, blog_id=blog_id, blog=blog)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog