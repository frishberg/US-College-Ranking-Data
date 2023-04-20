f = open("Included Schools.txt", "r")
names = []
for school in f.readlines() :
    names.append(school[:-1])
f.close()
print(names)