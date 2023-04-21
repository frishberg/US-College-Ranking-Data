import os
from icrawler.builtin import GoogleImageCrawler
import time
import json

#param: name of celebrity
#this method downloads a picture of the desired celebrity to the image folder of the webpage
def fetch_image(school_name) :
    filters = dict()
    google_Crawler = GoogleImageCrawler(storage = {'root_dir': 'logos'})
    google_Crawler.crawl(keyword = school_name + " square logo", max_num = 1, filters=filters)
    try :
        os.rename('logos/000001.jpg', 'logos/' + school_name + '.jpg')
    except FileNotFoundError :
        os.rename('logos/000001.png', 'logos/' + school_name + '.jpg')

def main() :
    f = open("Included Schools.txt", "r")
    for school in f.readlines() :
        school = school[:-1]
        if (not (os.path.exists("logos/" + school + ".jpg") or os.path.exists("logos/" + school + ".png"))) :
            fetch_image(school)
            print("Image fetched for " + school)
            time.sleep(1)
        else :
            print("Image already exists for " + school)
main()
