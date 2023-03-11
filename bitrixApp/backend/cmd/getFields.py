import requests, csv
import pandas as pd

def test1():
    df = pd.read_excel('fields.xlsx', dtype=str)

    df.to_csv(f"fieldsNew.xlsx", index=False, sep=';')


def test():
    dict = {}

    r = requests.get("https://finarbitr.bitrix24.ru/rest/9356/xzbva3ox6r0d1tqt/crm.deal.fields.json")
    result = r.json()

    for item in result['result']:
        dict[item] = result['result'][item]['title'], result['result'][item]['type']
        if "UF_CRM" in item:
            dict[item] = result['result'][item]['listLabel'], result['result'][item]['type']

    with open("fields.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Название", "Поле", "Тип"])
        for item in dict:
            writer.writerow([item, dict[item][0], dict[item][1]])

test()