import os

from fastapi import HTTPException, status
import models
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from sqlalchemy.orm.session import Session
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# THE SECRET KEY SHOULD BE EXTRACTED FROM THE ENVIRONMENT VARIABLES NOT HARDCODED
SECRET_KEY = '8d2205bff3068c2843fe1a2c462b506996814cfb167b882cf0e6c41288144442'
#SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_user_from_db(email: str, db: Session):
    return db.query(models.User).filter(models.User.email == email).first()

def authenticate_user(email: str, password: str, db):
    user = get_user_from_db(email, db)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def unauthorized_exception(msg):
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=msg,
        headers={"WWW-Authenticate": "Bearer"},
    )