import json

f = open("external-data/historical-usnews.json", "r")
data = json.load(f)
f.close()

rankings = []

f = open("included schools.txt", "r")
for school in f.readlines():
    school = school[:-1]
    for entry in data:
        if (entry["name"] == school):
            rankings.append(entry["2023"])
