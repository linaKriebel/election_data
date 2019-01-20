import csv
from main import add_party

row_length = 191

with open('btw.csv') as f:
  reader = csv.reader(f, delimiter=';')
  btw = list(reader)

#print (btw[2])

def get_parties():
  cells = btw[2]

  parties = []
  for cell in cells[19:]:
    if cell != '':
      parties.append(cell)
      add_party(cell)


  return parties

def get_districts():
  districts = []
  states = []
  for i in range(len(btw)):
    if i > 4:
      row = btw[i][0].split(';')
      if i < len(btw)-1:
        next_row = btw[i+1][0].split(';')
        if next_row[1] == '':
          #print('Found a state!')
          states.append(row[1])
        else:
          if row[1] != '':
            districts.append(row[1])
            #print(row[1])
      else:
        print('Bundesgebiet')

  print(districts)
  print(states)

#get_districts()
get_parties()


