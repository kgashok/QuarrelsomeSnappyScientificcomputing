
f = open("hype.csv")

content = f.read()

#print(content)
lines = content.split("\n")
#print(len(lines))

#print(lines[0])

col = lines[0].split(",")
#print(len(col))

db = {}

for line in lines[1:280]: 
  columns = line.split(",")
  if len(columns) == 78: 
    #print(columns)
    tech = columns[1]
    category = columns[-1]
    #print(tech, category)

    if len(category) and category not in db:
      db[category] = []
    if len(tech): 
      db[category].append(tech)

print(len(db))
import pprint

output_s = pprint.pformat(db)

with open('output.txt', 'wt') as out:
    pprint.pprint(db, stream=out)
    #pprint.pprint(output_s, stream=out)
