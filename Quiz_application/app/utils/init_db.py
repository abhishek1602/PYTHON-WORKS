from app.model.model import Base
from app.config.database import engine

def init_db():
    Base.metadata.create_all(bind= engine)

    