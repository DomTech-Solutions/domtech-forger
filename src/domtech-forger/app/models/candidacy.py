import uuid
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Candidacy(Base):
    __tablename__ = "candidacies"
    candidacy_id = Column(Integer, primary_key=True, index=True)
    politician_id = Column(UUID(as_uuid=True), ForeignKey("politicians.politician_id"), nullable=False)
    party_id = Column(Integer, ForeignKey("parties.party_id"), nullable=False)
    election_id = Column(Integer, ForeignKey("elections.election_id"), nullable=False)
    office = Column(String, nullable=False)
    electoral_number = Column(Integer, nullable=False)

    politician = relationship("Politician")
    party = relationship("Party")
    election = relationship("Election")