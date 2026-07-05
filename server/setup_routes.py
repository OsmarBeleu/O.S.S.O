import os

os.makedirs('app/api/v1/routes', exist_ok=True)

# __init__.py dos pacotes
for path in ['app/api/__init__.py', 'app/api/v1/__init__.py', 'app/api/v1/routes/__init__.py']:
    with open(path, 'w', encoding='utf-8') as f:
        f.write('')

# schemas de autenticação
os.makedirs('app/schemas', exist_ok=True)
with open('app/schemas/__init__.py', 'w', encoding='utf-8') as f:
    f.write('')

with open('app/schemas/auth.py', 'w', encoding='utf-8') as f:
    f.write(
        'from pydantic import BaseModel\n\n'
        'class RegisterRequest(BaseModel):\n'
        '    username: str\n'
        '    password: str\n'
        '    public_key: str\n\n'
        'class LoginRequest(BaseModel):\n'
        '    username: str\n'
        '    password: str\n\n'
        'class TokenResponse(BaseModel):\n'
        '    access_token: str\n'
        '    token_type: str = "bearer"\n'
        '    username: str\n'
    )
print('schemas/auth.py criado!')

# rotas de autenticação
with open('app/api/v1/routes/auth.py', 'w', encoding='utf-8') as f:
    f.write(
        'from fastapi import APIRouter, Depends, HTTPException, status\n'
        'from sqlalchemy.orm import Session\n'
        'from app.db.database import get_db\n'
        'from app.db.models.user import User\n'
        'from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse\n'
        'from app.services.auth_service import hash_password, verify_password, create_token\n\n'
        'router = APIRouter(prefix="/auth", tags=["auth"])\n\n'
        '@router.post("/register", status_code=201)\n'
        'def register(data: RegisterRequest, db: Session = Depends(get_db)):\n'
        '    existing = db.query(User).filter(User.username == data.username).first()\n'
        '    if existing:\n'
        '        raise HTTPException(status_code=400, detail="Username ja existe")\n'
        '    user = User(\n'
        '        username=data.username,\n'
        '        password=hash_password(data.password),\n'
        '        public_key=data.public_key\n'
        '    )\n'
        '    db.add(user)\n'
        '    db.commit()\n'
        '    db.refresh(user)\n'
        '    return {"message": "Usuário criado com sucesso"}\n\n'
        '@router.post("/login", response_model=TokenResponse)\n'
        'def login(data: LoginRequest, db: Session = Depends(get_db)):\n'
        '    user = db.query(User).filter(User.username == data.username).first()\n'
        '    if not user or not verify_password(data.password, user.password):\n'
        '        raise HTTPException(status_code=401, detail="Credenciais invalidas")\n'
        '    token = create_token({"sub": str(user.id), "username": user.username})\n'
        '    return TokenResponse(access_token=token, username=user.username)\n'
    )
print('routes/auth.py criado!')

# main.py
with open('main.py', 'w', encoding='utf-8') as f:
    f.write(
        'from fastapi import FastAPI\n'
        'from app.api.v1.routes import auth\n\n'
        'app = FastAPI(title="OSSO API")\n\n'
        'app.include_router(auth.router, prefix="/api/v1")\n\n'
        '@app.get("/")\n'
        'def root():\n'
        '    return {"status": "OSSO API rodando"}\n'
    )
print('main.py criado!')
print('Tudo criado com sucesso!')