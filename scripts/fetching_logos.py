from selenium import webdriver
import urllib.request

def main() :
    f = open("Included Schools.txt", "r")
    for school in f.readlines() :
        try :
            school = school[:-1]
            logo_url = fetch_logo(school)
            download_image_from_url(logo_url, "logos/" + school)
        except :
            print("Error with " + school)
    
def download_image_from_url(url, filename) :
    extension = url[url.rindex(".")+1:]
    urllib.request.urlretrieve(url, filename + "." + extension)

def fetch_logo(school_name) :
    from googlesearch import search
    google_results = search(school_name + " wikipedia", num_results=1, sleep_interval=1)
    wikipedia_link = ""
    for result in google_results :
        wikipedia_link = result
    logo_url = extract_wikipedia_logo_url(wikipedia_link)
    return logo_url

def extract_wikipedia_logo_url(link) : #using selenium
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(link)
    source = driver.page_source
    driver.close()
    source = source[source.index("og:image"):]
    source = source[source.index("content=")+9:]
    logo_url = source[:source.index('"')]
    print(logo_url)
    return logo_url


main()