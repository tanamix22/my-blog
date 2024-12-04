from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.faq_schemas import FaqCreate
from ..models import models
from ..schemas.faq_schemas import Faq as FaqSchema, FaqCreate, FaqUpdate
from ..database import SessionLocal, engine
from ..auth.jwt_bearer import JWTBearer
from ..crud import faq_crud as crud
from typing import List

models.Base.metadata.create_all(bind=engine)

router = APIRouter(tags=["faq"], prefix="/faqs")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=FaqSchema, dependencies=[Depends(JWTBearer())])
def create_faq(
    faq: FaqCreate,
    db: Session = Depends(get_db)
):
    return crud.create_faq(db=db, faq=faq)

@router.get("/", response_model=List[FaqSchema])
def read_faqs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    faqs = crud.get_faqs(db, skip=skip, limit=limit)
    return faqs

@router.get("/{faq_id}", response_model=FaqSchema, dependencies=[Depends(JWTBearer())])
def read_faq(faq_id: int, db: Session = Depends(get_db)):
    db_faq = crud.get_faq(db, faq_id=faq_id)
    if db_faq is None:
        raise HTTPException(status_code=404, detail="Faq not found")
    return db_faq

@router.put("/{faq_id}", response_model=FaqSchema, dependencies=[Depends(JWTBearer())])
def update_faq(
    faq_id: int,
    faq: FaqUpdate,
    db: Session = Depends(get_db)
):
    db_faq = crud.update_faq(db, faq_id=faq_id, faq=faq)
    if db_faq is None:
        raise HTTPException(status_code=404, detail="Faq not found")
    return db_faq

@router.delete("/{faq_id}", response_model=FaqSchema, dependencies=[Depends(JWTBearer())])
def delete_faq(faq_id: int, db: Session = Depends(get_db)):
    db_faq = crud.delete_faq(db, faq_id=faq_id)
    return db_faq