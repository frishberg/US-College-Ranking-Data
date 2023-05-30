import csv
import os
import json

f = open("external-data/historical-usnews.json", "r")
data = json.load(f)
f.close()

f = open("Included Schools.txt", "r")
schools = f.readlines()
f.close()

for school in schools :
    school = school.strip()
    rank = str(data[school]['2023'])
    print(rank)