from difflib import SequenceMatcher
import csv
import json

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

f = open("external-data/CSRankings.csv", "r", encoding="utf-8")
data = csv.DictReader(f)

g = open("Included Schools.txt", "r", encoding="utf-8")
schools = g.readlines()
g.close()

def school_name_match(school_name):
    cur_val = 0
    cur_school = ""
    for school in schools:
        school = school.strip()
        if similar(school_name, school) > cur_val and similar(school_name, school) > 0.9:
            cur_val = similar(school_name, school)
            cur_school = school
    return cur_school

json_data = {}

for row in data:
    name = (row["Institution"])
    ranking = (row["#"])
    ranking = int(ranking)
    school_name = school_name_match(name)
    if (school_name != ""):
        json_data[school_name] = ranking
    
with open("json-data/CSRankings.json", "w") as outfile:
    json.dump(json_data, outfile)