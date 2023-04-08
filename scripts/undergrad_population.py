from selenium import webdriver
import json

def main() :
    undergraduate_populations = {}
    f = open("Included Schools.txt", "r")
    for school in f.readlines() :
        school = school[:-1]
        curr_pop = int(fetch_undergraduate_population(school))
        undergraduate_populations[school] = curr_pop
        print(school + ": " + str(curr_pop))
    with open("undergraduate_populations.json", "w") as g :
        json.dump(undergraduate_populations, g)
    

def fetch_undergraduate_population(school_name) :
    from googlesearch import search
    google_results = search(school_name + " us news", num_results=1, sleep_interval=1)
    usnews_link = ""
    for result in google_results :
        usnews_link = result
    undergraduate_population = extract_usnews_undergraduate_population(usnews_link)
    return undergraduate_population

def extract_usnews_undergraduate_population(link) : #using selenium
    driver = webdriver.Chrome("scripts/chromedriver.exe")
    driver.get(link)
    source = driver.page_source
    if ('<p class="Paragraph-sc-1iyax29-0 lNNvk">Undergraduate Enrollment</p>' not in source) :
        return -1
    source = source[source.index('<p class="Paragraph-sc-1iyax29-0 lNNvk">Undergraduate Enrollment</p>'):]
    source = source[source.index('<p class="Paragraph-sc-1iyax29-0 kGlRjY">') + 41:]
    source = source[:source.index("<")].replace(",", "")
    return source

main()