from sqlalchemy.orm import Session
from . import models, schemas

def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Blog).offset(skip).limit(limit).all()

def create_blog(db: Session, blog: schemas.BlogCreate, image_url: str):
    db_blog = models.Blog(**blog.dict(), image_url=image_url)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()

def delete_blog(db: Session, blog_id: int):
    db_blog = get_blog(db, blog_id)
    if db_blog:
        db.delete(db_blog)
        db.commit()
    return db_blog