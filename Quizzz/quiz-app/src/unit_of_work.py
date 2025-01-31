from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base

class UnitOfWork:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None

    def __enter__(self):
        self.session = self.Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()

    def get_session(self):
        return self.session

    def initialize_database(self):
        Base.metadata.create_all(self.engine)