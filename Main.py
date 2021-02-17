from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)


def scrape():
    headers = ['v_mag', 'proper_name', 'bayer_designation',
               'ly', 'spectral_class', 'mass', 'radius', 'luminosity']
    stars_data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")

    for table in soup.find_all("table", attrs={"class", "wikitable sortable jquery-tablesorter"}):
        for tbody in soup.find_all("tbody"):
            for tr_tags in soup.find_all("tr"):
                for s in soup.select('th'):
                    s.extract()
                temp_list = []
                for index, tr_tag in enumerate(tr_tags):
                    try:
                        temp_list.append(tr_tag.contents[0].contents[0])
                    except:
                        for q in soup.select('span'):
                            q.extract()
                        try:
                            temp_list.append(tr_tag.contents[0])
                        except:
                            temp_list.append("")
                stars_data.append(temp_list)

    with open("Final.csv", "w", encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        for i in range(2, len(stars_data)):
            csvwriter.writerow(stars_data[i-1:i])


scrape()
