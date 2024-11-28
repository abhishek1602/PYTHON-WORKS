from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()

DATABASE_URL = "sqlite:///employeedatabase.db"

engine = create_engine(DATABASE_URL)

sessionlocal = sessionmaker(autoflush=False, bind=engine)


class Employees(Base):
    __tablename__ = "employee"
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String, nullable=False)
    emp_age = Column(Integer, nullable=False)
    emp_number = Column(Integer, nullable=False)
    emp_location = Column(String, nullable=False)
    emp_grade = Column(String, nullable=False)


Base.metadata.create_all(bind=engine)