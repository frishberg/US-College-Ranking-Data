import csv
from difflib import SequenceMatcher
import json

def similar(a, b) :
    return SequenceMatcher(None, a, b).ratio()

def main() :
    g = open("Included Schools.txt", "r")
    schools = g.readlines()
    g.close()

    json_data = {}

    f = open("external_data/QS-2022-ranking.csv", "r", encoding="utf8")
    reader = csv.reader(f)
    for row in reader :
        for school in schools :
            school = school[:-1]
            if similar(row[1], school) > 0.9 :
                rank = row[0]
                if ("=" in rank) : # if it's a tie it appears as "=297" instead of 297
                    rank = rank.replace("=", "")
                if ("-" in rank) : # if it's a range, like 801-1000, just take the lower bound
                    rank = rank.split("-")[0]
                print(row[1] + " matched with " + school + ".  Rank: " + rank)
                rank = int(rank)
                json_data[school] = rank
    f.close()

    with open("data/qs_rankings.json", "w") as outfile :
        json.dump(json_data, outfile)


main()
