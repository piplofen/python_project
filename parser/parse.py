import csv
from time import sleep

import requests
from bs4 import BeautifulSoup
import random

URL = "https://ecmb.online/fns/0000"

HOST = "https://ecmb.online/"

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
'accept': '*/*'}

PATH = "UFNS.csv"

ufns = []
subufns = []

def get_html(URL, retry = 5):
    try:
        r = requests.get(URL, headers = HEADERS)
        print(f"{URL} подключен")
        return r
    except Exception as e:
        if retry:
            print(f"Попыток осталось {retry}")
            return get_html(URL, retry = (retry - 1))


def save_file(items, path):
   with open(path, "w", newline = "") as file:
       writer = csv.writer(file, delimiter = ";")
       writer.writerow(["Код", "Наименование", "ИНН", "КПП", "Адрес", "Телефон", "email", "Сайт", "Дополнительно"])
       for item in items:
          writer.writerow([item["id"],item["name"],item["INN"],item["KPP"],item["adress"],item["phone"],item["email"],item["site"],item["id OKPO"]])

def get_content(html):
    soup = BeautifulSoup(html.text, 'html.parser')

    items = soup.find('tbody').find_all('td', class_='text-center')


    for item in items:
        subURL = HOST + item.find("a").get("href")
        try:
            sleep(random.randint(2, 5))
            subHtml = requests.get(subURL, headers = HEADERS)
            print(f"{subURL} подключен")
            if subHtml.status_code == 200:
                print(f"Статус код {subHtml.status_code}")
                subSoup = BeautifulSoup(subHtml.text, 'html.parser')
                bufer = []
                subItems = subSoup.find_all('table', class_='table')[2].get_text().splitlines()
                subLinks = subSoup.find('tbody').find_all('td', class_='text-center')

                for item in subItems:
                    bufer.append(item.partition(':')[2].strip())

                if len(bufer) == 10:
                    ufns.append({
                        "id" : bufer[1],
                        "name" : bufer[2],
                        "INN" : bufer[3],
                        "KPP" : bufer[4],
                        "adress" : bufer[5],
                        "phone" : bufer[6],
                        "email" : bufer[7],
                        "site" : bufer[8],
                        "id OKPO" : bufer[9]
                    })
                if len(bufer) == 9:
                    ufns.append({
                        "id": bufer[1],
                        "name": bufer[2],
                        "INN": bufer[3],
                        "KPP": bufer[4],
                        "adress": bufer[5],
                        "phone": bufer[6],
                        "email": bufer[7],
                        "site" : "-",
                        "id OKPO": bufer[8]
                    })

                if len(bufer) == 4:
                    ufns.append({
                        "id": bufer[1],
                        "name": bufer[2],
                        "INN": "-",
                        "KPP": "-",
                        "adress": "-",
                        "phone": "-",
                        "email": bufer[3],
                        "site": "-",
                        "id OKPO": "-"
                    })


                if len(bufer) == 6:
                    ufns.append({
                        "id": bufer[1],
                        "name": bufer[2],
                        "INN": "-",
                        "KPP": "-",
                        "adress": bufer[3],
                        "phone": "-",
                        "email": bufer[4],
                        "site": "-",
                        "id OKPO": bufer[5]
                    })

                if len(bufer) == 3:
                    ufns.append({
                        "id": bufer[1],
                        "name": bufer[2],
                        "INN": "-",
                        "KPP": "-",
                        "adress": "-",
                        "phone": "-",
                        "email": "-",
                        "site": "-",
                        "id OKPO": "-"
                    })

                if len(bufer) == 3:
                    ufns.append({
                        "id": bufer[1],
                        "name": bufer[2],
                        "INN": bufer[3],
                        "KPP": bufer[4],
                        "adress": bufer[5],
                        "phone": "-",
                        "email": "-",
                        "site": "-",
                        "id OKPO": "-"
                    })

                for item in subLinks:
                    subsubLinks = HOST + item.find("a").get("href")
                    try:
                        sleep(random.randint(2, 5))
                        subsubHtml = requests.get(subsubLinks, headers=HEADERS)
                        print(f"{subsubLinks} подключен")
                        if subsubHtml.status_code == 200:
                            print(f"Статус код {subsubHtml.status_code}")
                            subsubSoup = BeautifulSoup(subsubHtml.text, 'html.parser')
                            subbufer = []
                            subsubItems = subsubSoup.find_all('table', class_='table')[2].get_text().splitlines()

                            for item in subsubItems:
                                subbufer.append(item.partition(':')[2].strip())

                            if len(subbufer) == 10:
                                subufns.append({
                                    "id": subbufer[1],
                                    "name": subbufer[2],
                                    "INN": subbufer[3],
                                    "KPP": subbufer[4],
                                    "adress": subbufer[5],
                                    "phone": subbufer[6],
                                    "email": subbufer[7],
                                    "site": subbufer[8],
                                    "id OKPO": subbufer[9]
                                })

                            if len(subbufer) == 9:
                                ufns.append({
                                    "id": subbufer[1],
                                    "name": subbufer[2],
                                    "INN": subbufer[3],
                                    "KPP": subbufer[4],
                                    "adress": subbufer[5],
                                    "phone": subbufer[6],
                                    "email": subbufer[7],
                                    "site": "-",
                                    "id OKPO": subbufer[8]
                                })

                            if len(subbufer) == 4:
                                ufns.append({
                                    "id": subbufer[1],
                                    "name": subbufer[2],
                                    "INN": "-",
                                    "KPP": "-",
                                    "adress": "-",
                                    "phone": "-",
                                    "email": subbufer[3],
                                    "site": "-",
                                    "id OKPO": "-"
                                })

                            if len(subbufer) == 6:
                                ufns.append({
                                    "id": subbufer[1],
                                    "name": subbufer[2],
                                    "INN": "-",
                                    "KPP": "-",
                                    "adress": subbufer[3],
                                    "phone": "-",
                                    "email": subbufer[4],
                                    "site": "-",
                                    "id OKPO": subbufer[5]
                                })

                            if len(subbufer) == 3:
                                ufns.append({
                                    "id": subbufer[1],
                                    "name": subbufer[2],
                                    "INN": "-",
                                    "KPP": "-",
                                    "adress": "-",
                                    "phone": "-",
                                    "email": "-",
                                    "site": "-",
                                    "id OKPO": "-"
                                })

                            if len(subbufer) == 3:
                                ufns.append({
                                    "id": subbufer[1],
                                    "name": subbufer[2],
                                    "INN": subbufer[3],
                                    "KPP": subbufer[4],
                                    "adress": subbufer[5],
                                    "phone": "-",
                                    "email": "-",
                                    "site": "-",
                                    "id OKPO": "-"
                                })
                    except Exception as e:
                        print(e)

            save_file(ufns, PATH)

        except Exception as e:
            print(e)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(f"Статус код {html.status_code}")
        get_content(html)
    else:
        print("Ошибка подключения")
parse()