from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()

    def get(self, entity_class, entity_id):
        return self.session.query(entity_class).get(entity_id)

    def update(self, entity):
        self.session.merge(entity)
        self.session.commit()

    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()

    def all(self, entity_class):
        return self.session.query(entity_class).all()