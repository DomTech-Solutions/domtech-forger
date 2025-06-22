from app.db.base_class import Base
from app.db.session import engine

# Importe todos os modelos aqui para que o `create_all` os conheça
from app.models.user import User
from app.models.party import Party
from app.models.politician import Politician
from app.models.election import Election
from app.models.candidacy import Candidacy
from app.models.vote import Vote