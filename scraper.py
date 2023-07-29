from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# Brightest Stars URL 
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars" 

# Webdriver
service = Service(executable_path="C:/Users/aviji/OneDrive/Desktop/Project-C127-Web-Scraping-1/chromedriver.exe") 
browser = webdriver.Chrome(service=service) 
browser.get(START_URL)

time.sleep(10)

star_scraped_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    #Define Beautiful Soup object
    soup = BeautifulSoup(browser.page_source, "html.parser")

    #Find <table>
    bright_star_table = soup.find("table", attrs={"class", "wikitable"})

    # Find <tbody>
    table_body = bright_star_table.find('tbody')

    # Find <tr>
    table_rows = table_body.find_all('tr')

    # Get data from <td>

    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)

        temp_list = []

        for col_data in table_cols:
            #print(col_data.text)
            

            data = col_data.text.strip()
            # print(data)
            temp_list.append(data)

        #Append data to star_data list
        star_scraped_data.append(temp_list)
    
    stars_data = []

    for i in range(0, len(star_scraped_data)):

        Star_names = star_scraped_data[i][1]
        Distance = star_scraped_data[i][3]
        Mass = star_scraped_data[i][5]
        Radius = star_scraped_data[i][6]
        Lum = star_scraped_data[i][7]

        required_data = [Star_names, Distance, Mass, Radius, Lum]
        stars_data.append(required_data)

        #Define headers
        headers = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']

        #Define pandas DataFrame
        star_df_1 = pd.DataFrame(stars_data, columns=headers)

        #Convert to CSV
        star_df_1.to_csv("Scraped_Data_Stars.csv", index = True)

