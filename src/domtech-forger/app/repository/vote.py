from sqlalchemy.orm import Session
from typing import List, Optional
import uuid

from app.models.vote import Vote
from app.schemas.vote import VoteCreate

def create(db: Session, *, vote_in: VoteCreate, user_id: uuid.UUID) -> Vote:
    # O operador ** desempacota o dicionário do schema Pydantic nos argumentos do modelo SQLAlchemy
    db_obj = Vote(
        **vote_in.model_dump(),
        user_id=user_id
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj