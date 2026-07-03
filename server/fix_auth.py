with open('app/services/auth_service.py', 'w', encoding='utf-8') as f:
    f.write(
        'import bcrypt\n'
        'from jose import jwt\n'
        'from datetime import datetime, timedelta\n'
        'from app.core.config import settings\n\n'
        'def hash_password(password: str) -> str:\n'
        '    salt = bcrypt.gensalt()\n'
        '    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")\n\n'
        'def verify_password(plain: str, hashed: str) -> bool:\n'
        '    return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))\n\n'
        'def create_token(data: dict) -> str:\n'
        '    payload = data.copy()\n'
        '    payload["exp"] = datetime.utcnow() + timedelta(days=settings.access_token_expire_days)\n'
        '    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)\n'
    )
print('auth_service.py atualizado!')