import csv
import os
import json

csv_writer = csv.writer(open('data/all_data.csv', 'w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
headers = ["University Name", "Acceptance Rate", "Average SAT", "Niche Academic Grade", "Niche Athletic Grade", "Niche Campus Grade", "Niche Campus Food Grade", "Niche Diversity Grade", "Niche Dorms Grade", "Niche Location Grade", "Niche Overall Grade", "Niche Party Scene Grade", "Niche Professors Grade", "Niche Safety Grade", "Niche Student Life Grade", "Niche Value Grade", "Nobel Prizes", "QS World Rankings", "Undergraduate Population"]
csv_writer.writerow(headers)
        


f = open("Included Schools.txt", "r")
schools = f.readlines()
f.close()

for school in schools :
    school_data = []
    school_data.append(school.strip())
    for filename in os.listdir("data") :
        if (filename == "all_data.csv") :
            continue
        f = open("data/" + filename, "r")
        data = json.load(f)
        f.close()
        if (school.strip() not in data) :
            school_data.append("")
        else :
            school_data.append(data[school.strip()])
    csv_writer.writerow(school_data)