from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random

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
     acc1 = ' '
     print('---------------------------------------------------------------------------------')
     print('|                        type your complete name                                |')
     print('---------------------------------------------------------------------------------')
     name1 = input('')
     data = session.query(accounts).filter(accounts.name == name1)
     print(len(data))
     if type(data[0]) == "<class '__main__.accounts'>":
          print('---------------------------------------------------------------------------------')
          print('|                             you has a account                                 |')
          print('---------------------------------------------------------------------------------')
          __main__()   
     else:
          print('---------------------------------------------------------------------------------')
          print('|                             type your document                                |')
          print('---------------------------------------------------------------------------------') 
          document1 = input('')
          password1 = input('')
     office1 = '0000000000'
     for x in range(0,12):
          acc1+= f'{random.randint(0,9)}'
     
     data_insert = accounts(doc = document1, name= name1, acc = acc1, office = office1, credit = 1000, balance = 0, password = password1)
     session.add(data_insert)
     session.commit()
__main__()