import json
#file_name = input("What is the name of the json file? ")
file_name = "qs_rankings"
f = open("data/" + file_name + ".json", "r")
data = json.load(f)
f.close()

arr = []
f = open("Included Schools.txt", "r")
for school in f.readlines() :
    school = school[:-1]
    arr.append(data[school])

print(arr)