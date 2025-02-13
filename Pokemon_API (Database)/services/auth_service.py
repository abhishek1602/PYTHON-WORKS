from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from config.settings import app_config
 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
 
def create_access_token(data: dict):
    to_encode = data.copy()
    expire_minutes = int(app_config['ACCESS_TOKEN_EXPIRE_MINUTES'])
    expire = datetime.utcnow() + timedelta(minutes=expire_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode,app_config['SECRET_KEY'], algorithm=app_config['ALGORITHM'])
 
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
 
def get_password_hash(password: str):
    return pwd_context.hash(password)