import json

f = open("included schools.txt", "r", encoding="utf-8")
schools = f.readlines()
f.close()

schools = [school.strip() for school in schools]
f = open("json-data/CSRankings.json", "r", encoding="utf-8")
json_data = json.load(f)
f.close()

for school in schools:
    if school not in json_data:
        print("Not Available")
    else :
        print(json_data[school])