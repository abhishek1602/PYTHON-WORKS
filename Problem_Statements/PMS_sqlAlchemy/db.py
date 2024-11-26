from sqlalchemy import create_engine, Integer, Float, String, Column
from sqlalchemy.orm import declarative_base,sessionmaker


Base = declarative_base()

DATABASE_URL = "sqlite:///productdatabase.db"

engine = create_engine(DATABASE_URL)

sessionlocal = sessionmaker(autoflush=False, bind = engine)


class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable= False)
    product_price = Column(Float, nullable=False)


Base.metadata.create_all(bind = engine)




