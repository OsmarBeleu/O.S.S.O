import os

os.makedirs('app/db/models', exist_ok=True)
os.makedirs('app/services', exist_ok=True)

# user.py
with open('app/db/models/user.py', 'w', encoding='utf-8') as f:
    f.write(
        'from sqlalchemy import Column, String, DateTime\n'
        'from sqlalchemy.dialects.postgresql import UUID\n'
        'from datetime import datetime\n'
        'import uuid\n'
        'from app.db.database import Base\n\n'
        'class User(Base):\n'
        '    __tablename__ = "users"\n'
        '    id         = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)\n'
        '    username   = Column(String(32), unique=True, nullable=False)\n'
        '    password   = Column(String(255), nullable=False)\n'
        '    public_key = Column(String, nullable=False)\n'
        '    created_at = Column(DateTime, default=datetime.utcnow)\n'
    )
print('user.py criado!')

# auth_service.py
with open('app/services/auth_service.py', 'w', encoding='utf-8') as f:
    f.write(
        'from passlib.context import CryptContext\n'
        'from jose import jwt\n'
        'from datetime import datetime, timedelta\n'
        'from app.core.config import settings\n\n'
        'pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")\n\n'
        'def hash_password(password: str) -> str:\n'
        '    return pwd_context.hash(password)\n\n'
        'def verify_password(plain: str, hashed: str) -> bool:\n'
        '    return pwd_context.verify(plain, hashed)\n\n'
        'def create_token(data: dict) -> str:\n'
        '    payload = data.copy()\n'
        '    payload["exp"] = datetime.utcnow() + timedelta(days=settings.access_token_expire_days)\n'
        '    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)\n'
    )
print('auth_service.py criado!')

with open('app/services/__init__.py', 'w', encoding='utf-8') as f:
    f.write('')
print('Tudo criado com sucesso!')