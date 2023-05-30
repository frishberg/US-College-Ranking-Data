import json
import csv

g = open("data.csv", "r", encoding="utf-8")
data = csv.DictReader(g)

json_data = {}
headings = data.fieldnames[1:]

for row in data :
    name = row["University Name"]
    json_data[name] = {}
    for heading in headings :
        json_data[name][heading] = row[heading]

f = open("data.json", "w", encoding="utf-8")
json.dump(json_data, f, indent=4)
f.close()