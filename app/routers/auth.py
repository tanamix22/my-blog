from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.schemas import User
from app.auth.jwt_manager import create_token

router = APIRouter()

@router.post("/login", tags=["auth"])
def login(user: User):
    if user.username == "admin" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content={"message": "Login successful", "token": token})