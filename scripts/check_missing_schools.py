import json

json_src = "json-data/CSRankings.json"
json_data = json.load(open(json_src, "r", encoding="utf-8"))

f = open("included schools.txt", "r", encoding="utf-8")
schools = f.readlines()
f.close()

schools = [school.strip() for school in schools]
for school in schools:
    if school not in json_data:
        print(school)