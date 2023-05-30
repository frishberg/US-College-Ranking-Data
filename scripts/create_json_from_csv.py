import json
import csv

g = open("data.csv", "r", encoding="utf-8")
data = csv.DictReader(g)

json_data = {}
headings = ["Acceptance Rate", "Average SAT", "Niche Academic Grade", "Niche Athletic Grade", "Niche Campus Grade", "Niche Campus Food Grade", "Niche Diversity Grade", "Niche Dorms Grade", "Niche Location Grade", "Niche Overall Grade", "Niche Party Scene Grade", "Niche Professors Grade", "Niche Safety Grade", "Niche Student Life Grade", "Niche Value Grade", "Nobel Prizes", "QS World Rankings", "Undergraduate Population", "2023 US News Ranking", "2022 QS World Ranking", "2023 THE World Ranking"]

for row in data :
    name = row["University Name"]
    json_data[name] = {}
    for heading in headings :
        json_data[name][heading] = row[heading]

f = open("data.json", "w", encoding="utf-8")
json.dump(json_data, f, indent=4)
f.close()