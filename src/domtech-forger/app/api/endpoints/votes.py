from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.vote import VoteCreate, VoteResponse
from app.repository import vote as vote_repository

router = APIRouter()

@router.post("/", response_model=VoteResponse, status_code=status.HTTP_201_CREATED, summary="Registrar um novo voto")
def create_vote(
    *,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    vote_in: VoteCreate
):
    """
    Cria um novo registro de voto para o usuário autenticado.
    """
    # A lógica para validar se a candidatura ou partido existem seria adicionada aqui
    vote = vote_repository.create(db=db, vote_in=vote_in, user_id=current_user.user_id)
    return vote