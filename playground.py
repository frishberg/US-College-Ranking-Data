import json

f = open("json-data/nobel_prizes.json", "r")
data = json.load(f)
f.close()

new_data = {}

for row in data :
    name = row
    val = int(data[row])
    new_data[name] = val

f = open("json-data/nobel_prizes.json", "w")
json.dump(new_data, f)
f.close()