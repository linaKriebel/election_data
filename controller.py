from flask import Flask, request
from flask_cors import CORS
from main import State, District, First, Second, Party, session
import json
from flask import jsonify

app = Flask(__name__)
CORS(app)

@app.route('/getAllStates')
def states():
  states = session.query(State).all()

  s = []
  for state in states:
    s.append({
      'id':state.id,
      'name':state.name
      })
  states_json = json.dumps(s)

  return jsonify(states_json)

@app.route('/getAllDistrictsOf')
def districts():
  id = request.args.get('id')

  districts = session.query(District).filter_by(state_id = id) 

  d = []
  for district in districts:
    d.append({
      'id':district.id,
      'name':district.name
      })
  districts_json = json.dumps(d)

  return jsonify(districts_json)

@app.route('/getVotesOf')
def votes():
  id = request.args.get('id')

  parties = session.query(Party).all()

  votes_list = []

  for party in parties:
    first_vote = session.query(First).filter_by(district_id = id).filter_by(party_id = party.id).first()
    second_vote = session.query(Second).filter_by(district_id = id).filter_by(party_id = party.id).first()

    vote = {
      'party':party.name,
      'first_vote':first_vote.votes,
      'second_vote':second_vote.votes
    }

    votes_list.append(vote)

  votes_json = json.dumps(votes_list)

  return jsonify(votes_json)

app.run(debug=True)