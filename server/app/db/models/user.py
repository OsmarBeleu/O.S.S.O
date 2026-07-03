from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    id         = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username   = Column(String(32), unique=True, nullable=False)
    password   = Column(String(255), nullable=False)
    public_key = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
