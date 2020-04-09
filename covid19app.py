"""
Date : 15/04/2020
Author : Suman Sigdel
File : CoronaVirus.app : Scrapes the Covid-19 data from dynamic JS sites, ie. coronavirus.app
"""

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
# Path to the Chromedriver
driver = webdriver.Chrome('/Users///chromedriver') 
res = driver.get("https://coronavirus.app/") 

def scrape_country_name():
    #res = requests.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML;")
    soup = BeautifulSoup(html, "lxml")
    #box = soup.findAll("div",{"class": "map-sidebar-section-content"})
    box = soup.find_all("div",{"class":"map-sidebar-section-item-title"})
    return(box)

#print(scrape_country_name())

def scrape_country_infectants() :
    #res = driver.get("https://coronavirus.app/")
    # res = requests.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML;")
    soup = BeautifulSoup(html, "lxml")
    # box = soup.findAll("div",{"class": "map-sidebar-section-content"})
    box = soup.find_all("div", {"class": "map-sidebar-section-item-nb infected"})
    return (box)


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
