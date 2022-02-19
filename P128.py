from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
import requests

#website to take data from
START_URL="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

#browser to open in
browser= webdriver.Chrome("C:/Users/ADMIN/Downloads/chromedriver_win32/chromedriver")

#connecting link and browser
browser.get(START_URL)

#break
time.sleep(10)

headers = ["Confirmed brown dwarfs orbiting primary stars","Unconfirmed brown dwarfs","Field brown dwarfs","Former brown dwarfs"]
webpage = requests.get(START_URL)
print(webpage)

soup = BeautifulSoup(webpage.text,'html.parser')
star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Confirmed_brown_dwarfs_orbiting_primary_stars=[]
Unconfirmed_brown_dwarfs=[]
Field_brown_dwarfs=[]
Former_brown_dwarfs=[]

for i in range(1,len(temp_list)):
    Confirmed_brown_dwarfs_orbiting_primary_stars.append(temp_list[i][1])
    Unconfirmed_brown_dwarfs.append(temp_list[i][3])
    Field_brown_dwarfs.append(temp_list[i][5])
    Former_brown_dwarfs.append(temp_list[i][6])

df=pd.DataFrame(list(zip(Confirmed_brown_dwarfs_orbiting_primary_stars,Unconfirmed_brown_dwarfs,Field_brown_dwarfs,Former_brown_dwarfs))
.columns["Confirmed brown dwarfs orbiting primary stars","Unconfirmed brown dwarfs","Field brown dwarfs","Former brown dwarfs"])
df.to_csv("Dwarf_stars")
