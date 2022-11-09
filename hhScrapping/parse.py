import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import os

urlPython = "https://kaliningrad.hh.ru/search/vacancy?area=41&area=113&schedule=remote&search_field=name&search_field=company_name&search_field=description&text=Python&from=suggest_post&page=0&hhtmFrom=vacancy_search_list"

s = Service("G:\\project\\chromedriver.exe")

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service = s, options = chrome_options)

data = []

FILE = 'data.csv'

def get_html(url, params = None):
    r = requests.get(url, params = params)
    return r

def get_content(url):
    driver.get(url)
    html = driver.page_source
    text_html = BS(html, "html.parser")
    all_jobs = text_html.find_all("span", class_="g-user-content")

    for item in all_jobs:
        data.append({
            "name": item.find("a", class_="bloko-link").text,
            "link": item.find("a", class_ = "bloko-link").get("href")
        })
        with open(FILE, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["Название", "Ссылка"])
            for i in data:
                writer.writerow([i["name"],i["link"]])
    return data

def get_pages_count(html):
    text_html = BS(html, "html.parser")
    pagination = text_html.find("div", class_="pager")
    if pagination:
        page_count = pagination.get_text().strip()[8:-6]
        return int(page_count)
    else:
        return 1

def parse(url):
    driver.get(url)
    html = driver.page_source
    #get_content(html)
    page_count = get_pages_count(html)
    for page in range(0, page_count):
        print(f"Парсинг страницы {page + 1} из {page_count}")
        urlPython = f"https://kaliningrad.hh.ru/search/vacancy?area=41&area=113&schedule=remote&search_field=name&search_field=company_name&search_field=description&text=Python&from=suggest_post&page={page}&hhtmFrom=vacancy_search_list"
        data = []
        data.extend(get_content(urlPython))
    driver.close()
    driver.quit()
    os.startfile(FILE)

parse(urlPython)