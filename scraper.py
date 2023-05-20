from selenium import webdriver
from selenium.webdriver.common import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Edge()
browser.get(START_URL)

time.sleep(10)

def scrape():

    for i in range(0, 10):
        print(f'Scrapper Page {i+1}.......')

        soup = BeautifulSoup(browser.page_source, "html.parser")

        current_page_num = int(soup.find_all("input", attrs={"class, "page_num", }))[0].get("value")

        for ul_tag in soup.find_all("ul", attrs={"class","exoplanet"}):
            li_tags = ul.tag.find_all("li")

            temp_list = []

            for index, li_tag in enumerate(li_tags):

                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])

                    except:
                        temp_list.append("")

            planets_data.append(temp_list)

print(planets_data[1])
                
browser.find_element(by=By.XPATH, value='')                    
scrape()

header = ["name", "light_years_away_from_earth", "planet_mass", "stellar_magnitide", "discovery_date"]
planets_df_1 = pd.DataFrame(planets_data, columns=header)
planets_df_1.to_csv('scraped_data.csv', index=True, index_label="id")
