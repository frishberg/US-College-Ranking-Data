import json

f = open("Included Schools.txt", "r", encoding="utf-8")
schools = f.readlines()
f.close()

f = open("json-data/RUR_reputation_rankings.json", "r", encoding="utf-8")
data = json.load(f)

for school in schools :
    school = school.strip()
    if school in data :
        print(data[school])
    else :
        print("No Ranking")