from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time
from tqdm import tqdm

url = "https://superakb.ru/catalogue/category/akkumuliatory-starternye_315/?city=%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%8F%D1%80%D1%81%D0%BA&page=1"

HOST = "https://superakb.ru"

s = Service("G:\\project\\chromedriver.exe")

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service = s, options = chrome_options)

k = 0

options = []

data = []

FILE = 'data.csv'

def get_content(url):
    global k, options
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(url)
    html = driver.page_source
    text_html = BS(html, "html.parser")
    all_product = text_html.find_all("div", class_ = "col-sm-12 col-md-4")
    try:
        for item in all_product:
            name = item.find("div", class_ = "promo__product-item_title").get_text().strip()
            price =  item.find("div", class_ = "_old").get_text().strip()[:-2]
            link = item.find("div", class_ = "promo__product-item_image").find("a").get("href")
            driver.get(HOST + link)
            html_for_options = driver.page_source
            text_html_for_options = BS(html_for_options, "html.parser")
            all_options = text_html_for_options.find("ul", class_ = "attributes-list")
            options.append(all_options.text)
            for i in range(len(options)):
                options[i] = options[i].split("\n")

                if len(options[i]) == 14:
                    data.append({
                        "name": name,
                        "price": price,
                        "code": options[i][1][9:] if options[i][1][9:] is not None else "-",
                        "amperage": options[i][2][15:] if options[i][2][15:] is not None else "-",
                        "capacity": options[i][3][9:] if options[i][3][9:] is not None else "-",
                        "voltage": options[i][4][24:] if options[i][4][24:] is not None else "-",
                        "terminals": options[i][5][8:] if options[i][5][8:] is not None else "-",
                        "polarity": options[i][6][12:] if options[i][6][12:] is not None else "-",
                        "length": options[i][7][7:] if options[i][7][7:] is not None else "-",
                        "width": options[i][8][8:] if options[i][8][8:] is not None else "-",
                        "height": options[i][9][8:] if options[i][9][8:] is not None else "-",
                        "weight": options[i][10][5:] if options[i][10][5:] is not None else "-",
                        "manufacturer": options[i][11][14:] if options[i][11][14:] is not None else "-",
                        "country": options[i][12][21:] if options[i][12][21:] is not None else "-",
                    })

                    with open(FILE, "w", newline="") as file:
                        writer = csv.writer(file, delimiter=";")
                        writer.writerow(["Название", "Цена, руб.", "Артикул", "Стартовый ток", "Емкость",
                                         "Номинальное напряжение", "Клемы", "Полярность", "Длина",
                                         "Ширина", "Высота", "Вес", "Изготовитель", "Страна производства"])
                        for i in data:
                            writer.writerow([i["name"], i["price"], i["code"], i["amperage"], i["capacity"],
                                             i["voltage"], i["terminals"], i["polarity"], i["length"],
                                             i["width"], i["height"], i["weight"], i["manufacturer"], i["country"]])

                elif len(options[i]) == 11:
                    data.append({
                        "name": name,
                        "price": price,
                        "code": options[i][1][9:] if options[i][1][9:] is not None else "-",
                        "amperage": options[i][2][15:] if options[i][2][15:] is not None else "-",
                        "capacity": options[i][3][9:] if options[i][3][9:] is not None else "-",
                        "voltage": options[i][4][24:] if options[i][4][24:] is not None else "-",
                        "terminals": options[i][5][8:] if options[i][5][8:] is not None else "-",
                        "polarity": options[i][6][12:] if options[i][6][12:] is not None else "-",
                        "length": options[i][7][7:] if options[i][7][7:] is not None else "-",
                        "width": options[i][8][8:] if options[i][8][8:] is not None else "-",
                        "height": options[i][9][8:] if options[i][9][8:] is not None else "-",
                        "weight": options[i][10][5:] if options[i][10][5:] is not None else "-",
                        "manufacturer": "-",
                        "country": "-",
                    })

                    with open(FILE, "w", newline="") as file:
                        writer = csv.writer(file, delimiter=";")
                        writer.writerow(["Название", "Цена, руб.", "Артикул", "Стартовый ток", "Емкость",
                                         "Номинальное напряжение", "Клемы", "Полярность", "Длина",
                                         "Ширина", "Высота", "Вес", "Изготовитель", "Страна производства"])
                        for i in data:
                            writer.writerow([i["name"], i["price"], i["code"], i["amperage"], i["capacity"],
                                             i["voltage"], i["terminals"], i["polarity"], i["length"],
                                             i["width"], i["height"], i["weight"], i["manufacturer"], i["country"]])

            driver.get(url)
            options = []

        return data

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

def get_pages_count(html):
    text_html = BS(html, "html.parser")
    pagination = text_html.find("ul", class_ = "pagination pagination-v1")
    if pagination:
        page_count = pagination.get_text().strip()[33:-23]
        return int(page_count)
    else:
        return 1

def parse(url):
    driver.get(url)
    html = driver.page_source
    page_count  = get_pages_count(html)
    for page in tqdm(range(0, page_count), desc = "Страница", unit = "стр."):
        url = f"https://superakb.ru/catalogue/category/akkumuliatory-starternye_315/?city=%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%8F%D1%80%D1%81%D0%BA&page={page}"
        data = []
        data.extend(get_content(url))
    driver.close()
    driver.quit()
    quit()

parse(url)