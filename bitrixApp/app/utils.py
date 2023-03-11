import base64
import csv
import datetime
import json
import os
from secrets import token_hex
import requests
import re
from uuid import getnode as mac
import wmi
import utils


def createToken():
    return token_hex(24)


def decoding(data):
    return base64.b64decode(data)


def encoding(data):
    enc = data.encode("ascii")
    encb = base64.b64encode(enc)
    return encb.decode('ascii')


def getMac():
    return ':'.join(re.findall('..', '%012x' % mac()))


def getSerial():
    a = wmi.WMI()
    return a.Win32_BaseBoard()[0].SerialNumber


def simpleLogin(id: str, password: str, type: int):
    try:
        if id != "" and password != "":
            r = requests.post(url=url, json={
                "id": f"{encoding(id)}", "password": f"{encoding(password)}",
                "type": f"{type}"
            })
            if r.status_code == 200:
                print(r.text)
                return True
            else:
                return False
    except:
        pass


def login(id: str, password: str, type:int, token:str):
    try:
        if id != "" and password != "":
            r = requests.post(url=url, json={
                "id": f"{encoding(id)}", "password": f"{encoding(password)}",
                "mac": f"{encoding(getMac())}", "serial": f"{encoding(getSerial())}",
                "type": f"{type}", "token": f"{encoding(token)}"

            })

            if r.status_code == 200:
                print(r.text)
                return True
            else:
                return False

    except:
        return False


# def login(id: str, password: str, rb: bool):
#     try:
#         token = createToken()
#         if id != "" and password != "":
#             r = requests.post(url=url, json={
#                     "id": f"{encoding(id)}", "password": f"{encoding(password)}", "token": f"{encoding(token)}",
#                     "mac": f"{encoding(getMac())}", "serial": f"{encoding(getSerial())}"
#
#                 })
#             if r.status_code == 200:
#                 if rb:
#                     data = openFile("cfg", "json")
#                     if data:
#                         newdata = {
#                             id: {
#                                 "remember": True,
#                                 "password": encoding(password),
#                                 "token": encoding(token),
#                                 "mac": getMac(),
#                                 "serial": getSerial()
#                             }
#                         }
#                         data.update(newdata)
#                         writeFile("cfg", "json", "w", data)
#                     elif not data:
#                         newdata = {
#                             id: {
#                                 "remember": True,
#                                 "password": encoding(password),
#                                 "token": encoding(token),
#                                 "mac": getMac(),
#                                 "serial": getSerial()
#                             }
#                         }
#                         writeFile("cfg", "json", "w", newdata)
#                 else:
#                     data = openFile("cfg", "json")
#                     if data:
#                         newdata = {
#                             id: {
#                                 "remember": False,
#                                 "password": encoding(password),
#                                 "token": encoding(token),
#                                 "mac": getMac(),
#                                 "serial": getSerial()
#                             }
#                         }
#                         data.update(newdata)
#                         writeFile("cfg", "json", "w", data)
#                     elif not data:
#                         newdata = {
#                             id: {
#                                 "remember": False,
#                                 "password": encoding(password),
#                                 "token": encoding(token),
#                                 "mac": getMac(),
#                                 "serial": getSerial()
#                             }
#                         }
#                         writeFile("cfg", "json", "w", newdata)
#                 return True
#             elif r.status_code == 404:
#                 return False
#     except Exception as e:
#         print("except2", e)
#         return False


#  записываю файлик
def writeFile(path: str, type: str, param: str, data: object, print1=0):
    try:
        with open(f"{path}.{type}", param) as file:
            if type == "json":
                data = json.dump(data, file, indent=4)
            elif type == "csv":
                data = csv.writer(file)  # ?
        if print1 == 1:
            print(f"Файл {path}.{type} записан успешно")
    except FileNotFoundError as e:
        makeDir(path)
        writeFile(path, type, param, data)
    except Exception as e:
        print(e)


# создает новую папку(/путь, имя папки)
def newDir(path, name):
    try:
        return os.mkdir(path + "/" + name)
    except Exception as e:
        print(e)


# смотрит существует ли папка, если ее нет то создает
def checkDir(path):
    lclpath = path
    if os.path.exists(path):
        return False
    else:
        path = path.split("/")
        path.pop()
        path.pop(0)
        item = ""
        for i in range(len(path)):
            item += "/" + path[i]
            if os.path.exists(item):
                pass
            else:
                item = item.rpartition('/')[0]
                # print('/'.join(item.split('/')[:-1]), "AFTER")
                newDir(item, path[i])
                if item != lclpath:
                    return True
                else:
                    return False


# создает все до конечной папки
def makeDir(path):
    x = True
    while x:
        x = checkDir(path)


# открываю файлик
def openFile(path: str, type: str = None):
    try:
        with open(f"{path}.{type}", encoding="utf-8") as file:  # !!!!!!!!!!!!!!!!! encoding="utf-8" !!!!!!!!!!!!!!!!!
            if type == "json":
                data = json.load(file)
            elif type == "csv":
                data = csv.reader(file, delimiter=";")
            elif type is None:
                return file

        return data
    except Exception as e:
        print(e)
        return False


def deleteBirthdate(data):
    if (data == "") or (data == None):
        return "01.01.1970"
    else:
        return str(datetime.datetime.fromisoformat(data).date())