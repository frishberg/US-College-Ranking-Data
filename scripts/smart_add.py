import json
from difflib import SequenceMatcher

desired_file_name = input("What should the json file be called? (excluded .json) ")
desired_file_name = "data/" + desired_file_name + ".json"

f = open(desired_file_name, "w")
f.write("")

g = open("Included Schools.txt", "r")
schools = g.readlines()
g.close()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_closest_match(school, schools) :
    max_ratio = 0
    max_school = ""
    for s in schools :
        s = s[:-1]
        ratio = similar(school, s)
        if ratio>max_ratio :
            max_ratio = ratio
            max_school = s
    return max_school

result = {}
curr = ""

while (curr!="stop") :
    curr = input("What is the name of the current college? ")
    if curr=="stop" :
        break
    curr = find_closest_match(curr, schools)
    print(curr)
    num = input("How many nobel prizes did they win? ")
    if (num!=-1) :
        result[curr] = num

f.write(json.dumps(result))