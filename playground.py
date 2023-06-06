import json

f = open("data.json", "r")
data = json.load(f)
f.close()

f = open("included schools.txt", "r")
schools = f.readlines()
f.close()

json_data = {}

for school in schools:
    school = school.strip()
    json_data[school] = int(data[school]["2023 US News Ranking"])

f = open("json-data/2023_usnews_rankings.json", "w")
json.dump(json_data, f)