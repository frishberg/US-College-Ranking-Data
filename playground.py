import csv
import os
import json

f = open("json-data/2022_qs_world_ranking.json", "r")
data = json.load(f)
f.close()

f = open("Included Schools.txt", "r")
schools = f.readlines()
f.close()

for school in schools :
    school = school.strip()
    print(data[school])