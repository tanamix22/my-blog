from fastapi import FastAPI
from .routers import blog
from .database import Base, engine
from . import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blog.router)