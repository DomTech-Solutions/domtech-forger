import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Vote(Base):
    __tablename__ = "votes"
    vote_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    election_id = Column(Integer, ForeignKey("elections.election_id"), nullable=False)
    office = Column(String, nullable=False)
    vote_type = Column(String, nullable=False)
    candidacy_id = Column(Integer, ForeignKey("candidacies.candidacy_id"), nullable=True)
    party_id = Column(Integer, ForeignKey("parties.party_id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    owner = relationship("User", back_populates="votes")
    election = relationship("Election")
    candidacy = relationship("Candidacy")
    party = relationship("Party")