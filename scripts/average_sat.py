from selenium import webdriver
import json

def main() :
    average_sats = {}
    f = open("Included Schools.txt", "r")
    for school in f.readlines() :
        school = school[:-1]
        curr_sat = int(fetch_average_sat(school))
        average_sats[school] = curr_sat
        print(school + ": " + str(curr_sat))
    with open("average_sat.json", "w") as g :
        json.dump(average_sats, g)
    

def fetch_average_sat(school_name) :
    from googlesearch import search
    google_results = search(school_name + " us news", num_results=1, sleep_interval=1)
    usnews_link = ""
    for result in google_results :
        usnews_link = result
    average_sat = extract_usnews_average_sat(usnews_link)
    return average_sat

def extract_usnews_average_sat(link) : #using selenium
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(link)
    source = driver.page_source
    if ('<p class="Paragraph-sc-1iyax29-0 lNNvk">SAT Range*</p>' not in source) :
        return "-1"
    source = source[source.index('<p class="Paragraph-sc-1iyax29-0 lNNvk">SAT Range*</p>'):]
    source = source[source.index("Paragraph-sc-1iyax29-0 kGlRjY"):]
    range = source[source.index(">")+1:source.index("<")]
    first_val = int(range[:range.index("-")])
    second_val = int(range[range.index("-")+1:])
    average_score = (first_val + second_val) / 2
    return average_score

main()