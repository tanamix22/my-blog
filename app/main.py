from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles

from app.auth.jwt_bearer import JWTBearer

from .routers import blog, auth
from .database import Base, engine
from .models import models

from fastapi.security import HTTPBearer

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Montar la ruta estática para las imágenes
app.mount("/images", StaticFiles(directory="images"), name="images")

app.include_router(auth.router)
app.include_router(blog.router, dependencies=[Depends(JWTBearer())])