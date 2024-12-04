from sqlalchemy.orm import Session
from ..models.faq_models import Faq
from ..schemas.faq_schemas import FaqCreate, FaqUpdate

def get_faq(db: Session, faq_id: int):
    return db.query(Faq).filter(Faq.id == faq_id).first()

def get_faqs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Faq).offset(skip).limit(limit).all()

def create_faq(db: Session, faq: FaqCreate):
    db_faq = Faq(title=faq.title, description=faq.description)
    db.add(db_faq)
    db.commit()
    db.refresh(db_faq)
    return db_faq

def update_faq(db: Session, faq_id: int, faq: FaqUpdate):
    db_faq = get_faq(db, faq_id)
    if db_faq:
        db_faq.title = faq.title
        db_faq.description = faq.description
        db.commit()
        db.refresh(db_faq)
    return db_faq

def delete_faq(db: Session, faq_id: int):
    db_faq = get_faq(db, faq_id)
    if db_faq:
        db.delete(db_faq)
        db.commit()
    return db_faq

