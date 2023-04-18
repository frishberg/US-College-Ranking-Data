import json

f = open("usnews rankings archive.json", "r")
data = json.load(f)
f.close()

rankings = []

f = open("Included Schools.txt", "r")
for school in f.readlines():
    school = school[:-1]
    for entry in data:
        if (entry["name"] == school):
            rankings.append(entry["2023"])
