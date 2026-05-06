from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "segredo_super_secreto"
ALGORITHM = "HS256"

def hash_senha(senha: str):
    senha = senha[:72]
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash: str):
    senha = senha[:72]
    return pwd_context.verify(senha, hash)

def criar_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=1)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)