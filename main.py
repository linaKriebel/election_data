from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer , Column , String, ForeignKey  

engine = create_engine('sqlite:///election_data.db') 
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base() 
class State(Base):
  __tablename__ = 'states'
  id = Column(Integer , primary_key=True) 
  name = Column(String)
  # this attribute makes access to comments easier 
  electoral_districts = relationship("District")

class District(Base):
  __tablename__ = 'electoral_districts'
  id = Column(Integer , primary_key=True) 
  name = Column(String)
  # this comment belongs to the entry with this ID 
  state_id = Column(Integer , ForeignKey("states.id")) 
  # this attribute makes access to entry easier
  state = relationship("State")

class Party(Base):
  __tablename__ = 'parties'
  id = Column(Integer , primary_key=True) 
  name = Column(String)

class First(Base):
  __tablename__ = 'first_votes'
  id = Column(Integer , primary_key=True) 
  votes = Column(Integer)
  district_id = Column(Integer , ForeignKey("electoral_districts.id")) 
  party_id = Column(Integer , ForeignKey("parties.id"))

class Second(Base):
  __tablename__ = 'second_votes'
  id = Column(Integer , primary_key=True) 
  votes = Column(Integer)
  district_id = Column(Integer , ForeignKey("electoral_districts.id")) 
  party_id = Column(Integer , ForeignKey("parties.id"))



def add_party(name):
  new_party = Party(name = name) 
  session.add(new_party)
  session.commit()

#Base.metadata.create_all(engine)