import os

def perform_replace(file_name, original, new) :
    if (".git" not in file_name and os.path.isfile(file_name) and file_name!="rename.py") :
        f = open(file_name, "r")
        read = f.read()
        read = read.replace(original, new)
        f.close()

        f = open(file_name, "w")
        f.write(read)
        f.close()

        print(file_name + " sucessful")

def do_the_thing(file_name) :
    perform_replace(file_name, "Yeshiva", "Yeshiva University")

for file_name in os.listdir() :
    do_the_thing(file_name)

for file_name in os.listdir("data") :
    do_the_thing("data/" + file_name)
