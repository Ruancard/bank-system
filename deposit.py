from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:admin@localhost:5432/banco")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class accounts(Base):
     __tablename__ = "accounts"

     doc = Column(String, primary_key=True)
     name = Column(String, nullable=False)
     acc = Column(String, nullable=False)
     office = Column(String, nullable=False)
     credit = Column(Integer)
     balance = Column(Integer)
     password = Column(String, nullable=False)

     def __repr__(self):
          return f"cliente [name={self.name}]"

data_insert = accounts(doc = '44130945913', name='ruan cardoso moreira', acc = '192051934012', office = '110160', credit = 1000, balance = 5000, password = '237913')
session.add(data_insert)
session.commit()
