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

#Base.metadata.create_all(engine)

#### INSERT functions

def add_state(name):
  new_state = State(name = name)
  session.add(new_state)
  session.commit()

def add_district(name, state_name):
  state = session.query(State).filter_by(name = state_name).first()
  state_id = state.id

  new_district = District(name = name, state_id = state_id)
  session.add(new_district)
  session.commit()

def add_party(name):
  new_party = Party(name = name) 
  session.add(new_party)
  session.commit()

def add_first_vote(district_name, party_name, votes):
  district = session.query(District).filter_by(name = district_name).first()
  district_id = district.id

  party = session.query(Party).filter_by(name = party_name).first()
  party_id = party.id

  new_first_vote = First(votes = votes, district_id = district_id, party_id = party_id)
  session.add(new_first_vote)
  session.commit()

def add_second_vote(district_name, party_name, votes):
  district = session.query(District).filter_by(name = district_name).first()
  district_id = district.id

  party = session.query(Party).filter_by(name = party_name).first()
  party_id = party.id

  new_second_vote = Second(votes = votes, district_id = district_id, party_id = party_id)
  session.add(new_second_vote)
  session.commit()
