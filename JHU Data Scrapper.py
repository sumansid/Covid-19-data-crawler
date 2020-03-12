"""
Date : 11/04/2020
Author : Suman Sigdel
File : JHU Data Scrapper : Scrapes the Covid-19 data and puts in an excel file
"""
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('/Users/sumansigdel/Documents/chromedriver')
driver.get("https://coronavirus.app/")

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
driver = webdriver.Chrome('/Users/sumansigdel/Documents/chromedriver')


res = driver.get("https://coronavirus.jhu.edu/map.html")
#res = requests.get(url)
html = driver.execute_script("return document.documentElement.outerHTML;")

soup = BeautifulSoup(html, "lxml")
box = soup.find("div",{"class": "map-sidebar-section-content"})
print(box)


