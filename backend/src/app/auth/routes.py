from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.database import SessionLocal
from models.user import Usuario
from .schemas import UserCreate, UserLogin, Token
from .service import hash_senha, verificar_senha, criar_token

router = APIRouter(prefix="/auth", tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# REGISTER
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existente = db.query(Usuario).filter(Usuario.email == user.email).first()
    
    if existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    novo = Usuario(
        nome=user.nome,
        email=user.email,
        senha_hash=hash_senha(user.senha)
    )

    db.add(novo)
    db.commit()
    db.refresh(novo)

    return {"msg": "Usuário criado com sucesso"}

# LOGIN
@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(Usuario).filter(Usuario.email == user.email).first()

    if not db_user or not verificar_senha(user.senha, db_user.senha_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = criar_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }