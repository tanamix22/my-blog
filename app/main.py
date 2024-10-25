from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import blog
from .database import Base, engine
from . import models

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Montar la ruta estática para las imágenes
app.mount("/images", StaticFiles(directory="images"), name="images")

app.include_router(blog.router)