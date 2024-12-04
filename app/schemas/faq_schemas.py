from pydantic import BaseModel

class FaqBase(BaseModel):
    title: str
    description: str

class FaqCreate(FaqBase):
    pass

class FaqUpdate(FaqBase):
    pass

class FaqDelete(FaqBase):
    pass

class Faq(FaqBase):
    id: int

    class Config:
        orm_mode = True