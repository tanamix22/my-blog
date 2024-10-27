from jwt import encode, decode

# Configuración JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def create_token(data: dict):
    token: str = encode(payload=data, key=SECRET_KEY, algorithm=ALGORITHM)
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
    return data