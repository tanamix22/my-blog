from sqlalchemy.orm import Session
from ..models import models
from ..schemas import schemas

def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Blog).offset(skip).limit(limit).all()

def create_blog(db: Session, blog: schemas.BlogCreate):
    db_blog = models.Blog(**blog.dict())
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

def update_blog(db: Session, blog_id: int, blog: schemas.BlogUpdate):
    db_blog = get_blog(db, blog_id)
    if db_blog:
        for key, value in blog.dict().items():
            setattr(db_blog, key, value)
        db.commit()
        db.refresh(db_blog)
    return db_blog