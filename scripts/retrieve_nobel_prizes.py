from selenium import webdriver
import json

def main() :
    driver = webdriver.Chrome("scripts/chromedriver.exe")
    driver.get("https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_university_affiliation")
    source = driver.page_source
    links_found = []
    while ("href" in source) :
        source = source[source.index("href")+6:]
        link = source[:source.index('"')]
        if ("wiki" in link) :
            links_found.append(link)
    dict = convert_list_to_dict_with_number_of_occurences(links_found)
    f = open("output.txt", "a")
    for item in sort_dict(dict) :
        f.write(str(item) + '\n')

def convert_list_to_dict_with_number_of_occurences(list) :
    dict = {}
    for item in list :
        if (item in dict) :
            dict[item] += 1
        else :
            dict[item] = 1
    return dict

def sort_dict(dict) :
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)

#after the file generated, I went through and found all colleges in the US.

main()