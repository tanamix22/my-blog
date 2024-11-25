from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    content: str
    image_url: str

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    image_url: str  # Nuevo campo para la URL de la imagen

    class Config:
        orm_mode = True

class User(BaseModel):
    username: str
    password: str