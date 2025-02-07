from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt
import datetime

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "tajni_kljuc"

users_db = {}  # Privremena baza (kasnije zamijeniti s DynamoDB)

class User(BaseModel):
    username: str
    password: str

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)

def create_jwt_token(data: dict):
    return jwt.encode({"exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1), **data}, SECRET_KEY, algorithm="HS256")

@router.post("/register")
def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Korisnik već postoji")
    users_db[user.username] = hash_password(user.password)
    return {"message": "Registracija uspješna"}

@router.post("/login")
def login(user: User):
    if user.username not in users_db or not verify_password(user.password, users_db[user.username]):
        raise HTTPException(status_code=400, detail="Pogrešno korisničko ime ili lozinka")
    token = create_jwt_token({"sub": user.username})
    return {"access_token": token}
