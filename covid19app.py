"""
Date : 25/05/2020
Author : Suman Sigdel
File : CoronaVirus.app : Scrapes the Covid-19 data and puts in an excel file
"""

from bs4 import BeautifulSoup
#import requests
from selenium import webdriver
driver = webdriver.Chrome("/Users/sumansigdel/Desktop/chromedriver")
res = driver.get("https://coronavirus.app/")
html = driver.execute_script("return document.documentElement.outerHTML;")
soup = BeautifulSoup(html, "lxml")

def scrape_country_name():
    box = soup.find_all("div",{"class":"map-sidebar-section-item-title"})
    print(box)
    return box

def scrape_country_infectants() :
    box = soup.find_all("div", {"class": "map-sidebar-section-item-nb infected"})
    print(box)
    return box


def infectants_array():
    returned_data = scrape_country_infectants()
    infect_array = [row.text for row in returned_data]
    return infect_array

def countries_array():
    country_returned_data = scrape_country_name()
    return_array = [row.text for row in country_returned_data]
    return return_array

def array_to_dict():
    dictionary = dict(zip(countries_array(), infectants_array()))
    return dictionary
