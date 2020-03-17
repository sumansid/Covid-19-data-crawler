"""
Date : 11/04/2020
Author : Suman Sigdel
File : CoronaVirus.app : Scrapes the Covid-19 data using Selenium Webdriver and BeautifulSoup
"""

from bs4 import BeautifulSoup
import requests
from selenium import webdriver

driver = webdriver.Chrome('/Users/sumansigdel/Documents/chromedriver')

def scrape_country_name():
    res = driver.get("https://coronavirus.app/")
    #res = requests.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML;")

    soup = BeautifulSoup(html, "lxml")
    #box = soup.findAll("div",{"class": "map-sidebar-section-content"})

    box = soup.find_all("div",{"class":"map-sidebar-section-item-title"})
    driver.quit()
    return(box)

#print(scrape_country_name())

def scrape_country_infectants() :
    res = driver.get("https://coronavirus.app/")
    # res = requests.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML;")

    soup = BeautifulSoup(html, "lxml")
    # box = soup.findAll("div",{"class": "map-sidebar-section-content"})

    box = soup.find_all("div", {"class": "map-sidebar-section-item-nb infected"})
    driver.quit()
    return (box)

print(scrape_country_infectants())
