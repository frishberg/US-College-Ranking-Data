import os
import json

def clear_file() :
    f = open("output.txt", "w")
    f.write("")
    f.close()

def toArray(json) :
    result = "["
    for item in json :
        result += '"' + str(json[item]) + '", '
    result = result[:-2]
    result += "]"
    return result

g = open("included schools.txt", "r")
schools = g.readlines()
g.close()

output = open("output.txt", "a")
school_string = "["
for school in schools :
    school_string += '"' + school.strip() + '", '
school_string = school_string[:-2]
school_string += "];"
output.write("var college_names = " + school_string + "\n")

clear_file()
for file in os.listdir("json-data") :
    s = "var " + file[:-5].replace("2023_", "").replace("2022_", "") + " = "
    arr = []
    if (file.endswith(".json")) :
        f = open("json-data/" + file, "r")
        data = json.load(f)
        f.close()
        for school in schools :
            school = school.strip()
            if school in data :
                arr.append(data[school])
            else :
                arr.append(0)
        s += str(arr)
        output.write(s + ";\n")