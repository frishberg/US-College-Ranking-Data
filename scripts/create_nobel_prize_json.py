#after running "retrieve_nobel_prizes.py", it will creates output.  Go through the file, using Ctrl F, and find all US universities.  Have "Included Schools.txt" open in another tab in VS Code, and go through, replacing the names to the maching names of Included Schools
import json

def main() :
    data = {}
    added = []
    f = open("scripts/output.txt")
    for line in f:
        name = line[:line.index(",")]
        count = line[line.index(",")+1:-1]
        data[name] = int(count)
        added.append(name)
    f.close()
    f = open("Included Schools.txt")
    for line in f:
        name = line[:-1]
        if name not in added:
            data[name] = 0
    f.close()
    json.dump(data, open("data/nobel_prizes.json", "w"))

main()