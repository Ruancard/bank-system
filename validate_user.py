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

def __main__():
     print('---------------------------------------------------------------------------------')
     print('|                           type your account number                            |')
     print('---------------------------------------------------------------------------------')
     x = input('')
     data = session.query(accounts).filter(accounts.acc == x)

     if data[0] != None:
          print('---------------------------------------------------------------------------------')
          print('|                hello ' + data[0].name + ' type your password                  |')
          print('---------------------------------------------------------------------------------')
          x = input('')
          if x == data[0].password:
               return data
          else:
               print('---------------------------------------------------------------------------------')
               print('|                             invalid password                                  |')
               print('---------------------------------------------------------------------------------')
               __main__()

     else:
          print('---------------------------------------------------------------------------------')
          print('|                             invalid account                                   |')
          print('---------------------------------------------------------------------------------')
          __main__()

__main__()
