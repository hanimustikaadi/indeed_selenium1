
from bs4 import BeautifulSoup
import time

from selenium import webdriver
import requests
import json
from bs4 import BeautifulSoup

import os
import pandas as pd


driver = webdriver.Chrome()
driver.get('https://www.indeed.com/jobs?q=python+developer&l=Remote&vjk=65fb815d935f6a4e')
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')

pages = soup.find('nav', attrs={'aria-label': 'pagination'}).find_all('div')
total = [page.text for page in pages]
print(int(max(total)))

soup = BeautifulSoup(html_content, 'html.parser')
products = soup.find_all(
        "table", attrs={"class": "jobCard_mainContent big6_visualChanges"}
    )
print(f"item found: {len(products)}")

job_list: list = []
test_list: list = []
for item in products:
    title = item.find("h2", attrs={"class": "jobTitle"}).text.strip()
    company = item.find("span", attrs={"class": "companyName"})
    company_name = company.text.strip()
    try:
           company_link = site + company.find("a")["href"]
    except:
           company_link = "Link not available"
    company_address = item.find(
        "div", attrs={"class": "companyLocation"}
    ).text.strip()




    # reformating data on dictionary
    data_dict: dict = {
    "job title": title,
    "company name": company_name,
    "company profile": company_link,
    "address": company_address.replace("•", ""),
    }

     # append to list
    job_list.append(data_dict)

    print(data_dict)

