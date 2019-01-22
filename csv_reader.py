import csv
from connector import add_state, add_district, add_party, add_first_vote, add_second_vote

#read csv lines as list of lists
print('Reading csv ...')
with open('btw.csv') as f:
  reader = csv.reader(f, delimiter=';')
  btw = list(reader)

print('Reading csv completed.')

row_count = len(btw)

parties = []
states = []
districts = []

party_map = {}
states_map = {}
district_map = {}
district_state_map = {}

# extract all parties
print('Adding parties ...')
party_row = btw[2]
i = 19 # start from column 20
for cell in party_row[19:]:
  if cell != '':
    parties.append(cell)
    party_map[cell] = i

    add_party(cell)
  i += 1

print('Adding parties completed.')

# extract all states and districts
print('Adding states and districts ...')
for i in range(row_count):
  # start from row 4
  if i > 4:
    cell = btw[i][1]

    # if not last row
    if i < row_count-1:
      next_row_cell = btw[i+1][1]
      if next_row_cell == '':
        states.append(cell)
        states_map[btw[i][0]] = cell

        add_state(cell)
      else:
        if cell != '':
          districts.append(cell)
          district_map[cell] = i
          district_state_map[cell] = btw[i][2]

print('Adding states and districts completed.')

print('Adding votes ...')
for district in districts:
  # map district to state
  state_no = district_state_map[district]
  state_name = states_map[state_no] 

  add_district(district, state_name)

  for party in parties:
    # extract first vote
    r = district_map[district]
    c = party_map[party]
    votes = btw[r][c]

    add_first_vote(district, party, votes)

    # extract second vote
    c = c+2
    votes = btw[r][c]

    add_second_vote(district, party, votes)

print('Adding votes completed.')
print('Reading csv completed.')
