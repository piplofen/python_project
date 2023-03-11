import csv
import pprint
import sys


sys.path.append('/var/razrab/backend')

import newFile
import utils as u
import mainView.model.bitrixTypeToBase as d


# # import pprint
# import newFile
# # import paramsView as pv
import pickle as pic
# from sys import argv


list1 = []
list2 = []

# tDeal = "testauto"
# pathFile = "deal.csv"

def getData():
    print(4)
    # data = u.openFile("fields/deal", "csv")
    # print(data)
    # reader = csv.reader(data)
    # print(reader)
    with open(path, "r", newline='', encoding="cp1251") as file:
        reader = csv.reader(file)
        for item in reader:
            row = item[0].split(";")
            # print(item)
            # print([unicode(cell, 'utf-8') for cell in row])
            row = item[0].split(";")
            # print(item)
            if row[3] == "1":
                list1.append([row[4], row[0], d.dictType[row[2]][1]])
                list2.append([row[4], d.dictType[row[2]][0]])
        if flag == 1:
            # print(435352356)
            # print(list1)
            print(list1)
            with open(f"../mainView/viewPython/{nameTable}.obj", 'wb') as f:
                pic.dump(list1, f)
            return list1  # для представления
        elif flag == 2:
            # print(534634634)
            # print(list2)
            print("2")
            with open(f"../mainView/viewBase/{nameTable}.obj", 'wb') as f:
                pic.dump(list1, f)
            if createTable == "True":
                print("пошел")
                db = newFile.Database()
                db.createTable(list2, nameTable)
            return list2  # для создания бд

def getTest():
    data = u.openFile("cmd/fields/inParams", "json")
    pprint.pprint(data)


# m = get(1)
# pv.getView(m)
# print("=======")
# pprint.pprint(list2)
# db.createTable(list2, tDeal)

#getTest()


if __name__ == "__main__":
    name, nameFileE, nameTable, flag, createTable = sys.argv
    flag = int(flag)
    path = f"fields/{nameFileE}"
    getData()

