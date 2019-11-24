from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


# parent base class
Base = declarative_base()

class Alchemy(Base):
    __tablename__ = "alchemy"

    id = Column('id', Integer, primary_key=True) #autoincrement=True
    name = Column('name', String)
    author = Column('author', String)

 
# engine  - specify dbms and db location
#   echo - dump the sql to terminal  
# engine  = create_engine('sqlite:///:memory:', echo=True)
engine  = create_engine('sqlite:///alchemy.db', echo=True)
# from pdb import set_trace; set_trace() # (pdb) engine then 'quit'

Base.metadata.create_all(bind=engine) # connects to the table in DB

Session = sessionmaker(bind=engine)
session = Session()
# OR session = sessionmaker(bind=engine)()

# Add data - uncomment when not adding data
# alchemy = Alchemy()
# alchemy.id = 2
# alchemy.name = "Lido"
# alchemy.author = "Ken"
# session.add(alchemy)
# session.commit()

# View data - uncomment when not needed
alchemies = session.query(Alchemy).all()
for alchemy in alchemies:
    print(f"alchemy object: {alchemy} author: {alchemy.author}")

session.close()
