from pydantic import BaseModel

class HomePageImageBase(BaseModel):
    image_url: str
    description: str

class HomePageImageCreate(HomePageImageBase):
    pass

class HomePageImageUpdate(HomePageImageBase):
    pass

class HomePageImage(HomePageImageBase):
    id: int

    class Config:
        orm_mode = True