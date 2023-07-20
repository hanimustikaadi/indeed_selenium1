import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

""" Konsep :
1. scraping indeed.com
py
2. user input :
2a. user input pekerjaan DONE
2b. user input lokasi DONE
2c. user input halaman DONE
3. dapatkan data html
4. scraping hasil html
5. masukan ke 
"""
"""
https://id.indeed.com/jobs?q={input pekerjaan}&l={input lokasi}&start={input halaman}&vjk=671ad2f62cc25cac
"""


def driver():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(200)
    driver.implicitly_wait(120)
    return driver


def target_url(url):
    driver.get(url)
    html_content = driver.page_source
    with open('target.html', 'w', encoding='utf-8') as file:
        soup = BeautifulSoup(html_content, 'html.parser')
        file.writelines(soup.prettify())


def input_pekerjaan():
    pekerjaan = input("Masukan pekerjaan :")
    return pekerjaan


def input_lokasi():
    lokasi = input("Masukan lokasi pekerjaan :")
    return lokasi


def input_halaman():
    halaman = input("Masukan halaman :")
    return int(halaman)


def calculate(n):
    if n == 1:
        return 1
    else:
        return (n - 1) * 10


def set_url(job, loc, pp):  # job = pekerjaan, loc = lokasi, pp = halaman
    url = f"https://id.indeed.com/jobs?q={job}&l={loc}&start={pp}"
    return url

def get_total_pages(url):
    driver = webdriver.Chrome()
    driver.get(f'{url}')
    html_content = driver.page_source

    # checking temporary file

    soup = BeautifulSoup(html_content, 'html.parser')
    pages = soup.find('nav', attrs={'aria-label': 'pagination'}).find_all('div')
    total = [page.text for page in pages]
    #print(int(max(total)))
    print(f"item page: {int(max(total))}")

def get_all_item(url):
    driver = webdriver.Chrome()
    driver.get(f'{url}')
    html_content = driver.page_source
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


if __name__ == "__main__":
    pekerjaan = input_pekerjaan()
    lokasi = input_lokasi()
    halaman = input_halaman()
    kalkulasi_halaman = str(calculate(n=halaman))
    #print(type(kalkulasi_halaman))
    url = set_url(pekerjaan, lokasi,kalkulasi_halaman)
    driver = driver()
    target_url(url=url)
    time.sleep(120)
    get_total_pages(url)
    get_all_item(url)