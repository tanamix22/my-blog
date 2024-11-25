from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from .routers import blog, auth
from .database import Base, engine
from .models import models

from fastapi.security import HTTPBearer

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",  # Agrega aquí los orígenes permitidos
    "https://terapias.netlify.app/",  # Agrega aquí tu dominio en producción
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar la ruta estática para las imágenes
app.mount("/images", StaticFiles(directory="images"), name="images")

app.include_router(auth.router)
app.include_router(blog.router)