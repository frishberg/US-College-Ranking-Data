import csv
import json

f = open('data.csv', 'r')
reader = csv.reader(f)
headers = ['University Name', 'Acceptance Rate', 'Average SAT', 'Niche Academic Grade', 'Niche Athletic Grade', 'Niche Campus Grade', 'Niche Campus Food Grade', 'Niche Diversity Grade', 'Niche Dorms Grade', 'Niche Location Grade', 'Niche Overall Grade', 'Niche Party Scene Grade', 'Niche Professors Grade', 'Niche Safety Grade', 'Niche Student Life Grade', 'Niche Value Grade', 'Nobel Prizes', 'QS World Rankings', 'Undergraduate Population', '2023 US News Ranking', '2022 QS World Ranking']

json_data = {}

def toInt(s) :
    #if the string can be a number
    if (s.isdigit()) :
        return int(s)
    else :
        return s

for row in reader:
    if (row[0] == 'University Name'):
        continue
    name = row[0]
    json_data[name] = {}
    for i in range(1, len(headers)):
        json_data[name][headers[i]] = toInt(row[i])
f.close()

f = open("data.json", "w")
f.write(json.dumps(json_data))
f.close()