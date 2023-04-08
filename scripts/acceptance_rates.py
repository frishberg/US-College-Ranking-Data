from selenium import webdriver
import json

def main() :
    acceptance_rates = {}
    f = open("Included Schools.txt", "r")
    for school in f.readlines() :
        school = school[:-1]
        curr_ar = int(fetch_acceptance_rate(school))
        acceptance_rates[school] = curr_ar
        print(school + ": " + str(curr_ar))
    with open("acceptance_rates.json", "w") as g :
        json.dump(acceptance_rates, g)
    

def fetch_acceptance_rate(school_name) :
    from googlesearch import search
    google_results = search(school_name + " us news", num_results=1, sleep_interval=1)
    rusnews_link = ""
    for result in google_results :
        usnews_link = result
    acceptance_rate = extract_usnews_acceptance_rate(usnews_link)
    return acceptance_rate

def extract_usnews_acceptance_rate(link) : #using selenium
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(link)
    source = driver.page_source
    if ('<p class="ApplyingSection__DataHeader-sc-2strss-7 hRHtQv">' not in source) :
        return "-1"
    source = source[source.index('<p class="ApplyingSection__DataHeader-sc-2strss-7 hRHtQv">'):]
    source = source[:source.index("%")]
    source = source[source.rindex(">") + 1:]
    return source

main()