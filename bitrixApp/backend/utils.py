import csv, json, requests, settings, datetime, math, time, os, logging as log
from secrets import token_hex
# from systemd import journal



def createToken():
    return token_hex(24)


# получаю состояние очереди
def que(url, sec=1):
    URL = url + f"?seconds={sec}"
    r = requests.get(URL, headers=settings.headersForQue)
    que = r.json()
    try:
        return math.ceil(que["seconds"])
    except:
        return 0


# import logging
# from systemd.journal import JournalHandler
#
# log = logging.getLogger('demo')
# log.addHandler(JournalHandler())
# log.setLevel(logging.INFO)
# log.info("sent to journal")

# функция ожидания очереди (нуждается в доработке(количество попыток(хранится в settings), записиь ошибок в лог))
def waitQue():
    x = que(settings.urlForQue)
    if x == 0:
        # journal.write("TEST")
        log.info("Очередь пуста. Можно идти.")
        print("Очередь пуста. Можно идти.")
        return True
    elif x > 0:
        log.info(f"Очередь занята на {x} секунд")
        print(f"Очередь занята на {x} секунд")
        log.info(f"Жду {x} секунд.")
        print(f"Жду {x} секунд.")
        time.sleep(x)
        waitQue()
        return False


# проверяю токен
def checkToken(text):
    if text["token"] == settings.token:
        return True
    else:
        return False


# записываю в файлик
def writeFile(path: str, type: str, param: str, data: object, print1=0):
    try:
        with open(f"{path}.{type}", param) as file:
            if type == "json":
                data = json.dump(data, file, indent=1)
            elif type == "csv":
                data = csv.writer(file)  # ?
        if print1 == 1:
            print(f"Файл {path}.{type} записан успешно")
    except FileNotFoundError as e:
        makeDir(path)
        writeFile(path, type, param, data)
    except Exception as e:
        log.error(f"{e}")


# создает новую папку(/путь, имя папки)
def newDir(path, name):
    try:
        return os.mkdir(path + "/" + name)
    except Exception as e:
        log.critical(f"utils (newDir) папка не создан.\nОшибка: {e}")


# смотрит существует ли папка, если ее нет то создает
def checkDir(path):
    lclpath = path
    if os.path.exists(path):
        log.critical(f"utils (checkDir) папка существует но файл не записан")
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


# получаю новый аксес и рефреш токен
def newRequest():
    dataJson = openFile("settings", "json")
    url = f"""https://oauth.bitrix.info/oauth/token/?grant_type=refresh_token&client_id={settings.C_REST_CLIENT_ID}&client_secret={settings.C_REST_CLIENT_SECRET}&refresh_token={dataJson["refresh_token"]}"""
    try:
        r = requests.get(url, headers=settings.HEADERS)
        value = r.json()
        writeFile("testMain", "json", "w", value)
        data = openFile("testMain", "json")
        dataJson["refresh_token"] = data["refresh_token"]
        dataJson["access_token"] = data["access_token"]
        dataJson["timeNewAccessToken"] = str(datetime.datetime.now())
        writeFile("settings", "json", "w", dataJson)
        return True
    except:
        return False


# проверка не просрочен ли токен
def checkDate(date):
    date1 = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    date2 = date1 + datetime.timedelta(minutes=59)
    if datetime.datetime.now() < date2:
        return True
    else:
        return False


# создаю логи
def logStart():  
    return log.basicConfig(level=settings.loggerLevel, encoding="utf-8", filename="/var/log/backend/log.log",
                           filemode="a", format="[%(asctime)s] - [%(levelname)s] - [%(filename)s.%(funcName)s(%("
                                                "lineno)d)] > [%(message)s]")


# форматирую дату если пустая и NONE
def deleteBirthdate(data):
    if (data == "") or (data == None):
        return "01.01.1970"
    else:
        return str(datetime.datetime.fromisoformat(data).date())


# Преобразует переменную val в заданный тип tip. param третий параметр преобразования

def isNone(var):
    if (var != None) and (var != "") and (var != []) \
            and (var != ()) and (var != {}):  # 1 & 0 -> 0
        return True
    else:
        return False


def convertType(val, tip, param="non"):
    # print(val, type(val),"->", tip)
    x = isNone(val)

    if x and param == "non":  # Если val не пустое и param == non
        if type(val) != f"'{tip}'":  # Если тип переменной не равен переданому типу
            if type(val) == list:
                res = convertLists(val)
                return res
            else:
                # if f"{tip}" == "list_str":
                #     # for item in val:
                #     #     res += f"{item} -"
                #     res = convertLists(val)
                #     print("Вход - ", res, type(res))
                #     print("==========================")
                #     return res
                # else:
                #     res = eval(f"{tip}('''{val}''')")
                #     print("Вход - ", res, type(res))
                #     print("==========================")
                #     return res
                res = eval(f"{tip}('''{val}''')")
                # print("Вход - ", res, type(res))
                # print("==========================")
                return res
        else:  # Если тип переменной равен выходному типу
            res = val
            # print("Вход - ", res, type(res))
            # print("==========================")
            return res
    elif not x and param == "non":  # Если val пустое
        res = ''
        # print("Вход - ", res, type(res))
        # print("==========================")
        return res
    # Похоже вообще нах не надо дальше
    elif not x and param != "non":
        # print("pfktntk c.lf")
        if f"{tip}" == "str":
            val = "0dgfasdges"
            return val
        elif f"{tip}" == "list_str":
            for item in val:
                res += f"{item} -"
                return res
        else:
            # print("Хуся")
            res = eval(f"{tip}('''{val}''')")
            return res


def execTuple(list):
    value = ""
    for item in list:
        if item == '':
            value += ", NULL"
        else:
            value += f",'{item}'"
    # res = value[1:]
    # print(value, type(value))
    return value[1:]

    # if param == "non":
    #     if isNone(val):
    #         print("NOT EMPTY")


# def convertType(val, tip, param="non"):
#
#     print(val, type(val), tip)
#
#     try:
#         log.info(f"{log}")
#         res = ""
#         if val != None and val != "" and val != []:
#             # print(val, 'в исключение не попал типа')
#             if type(val) != f"'{tip}'":
#                 if param == "non": res = eval(f"{tip}('{val}')") # int("4")
#                 else:
#                     print(tip, "tip")
#                     res = eval(f"{tip}('{val}','{param}')")
#             else: res = val
#         elif val is None:
#             print("Я попал в NONE")
#             val = "-"
#         elif val is []:
#             print("Я попал в NONE")
#             val = "-"
#         else:
#             if tip == "str":
#                 val = ""
#             elif tip == "int":
#                 val = 0
#             # print(val, 'в исключение попал типа')
#             # val = 00
#             res = eval(f"{tip}('{val}')")
#             # print(val)
#             #res = 00
#             # print(val, "val")
#             # print(res, "res")
#         return res
#     except:
#         log.info("Какая то ошибка")
# превращает список в строку
def convertLists(value):
    result = ""
    for vv in value:
        # print(vv)
        result += f",{str(vv)}"
        # result = result + str(vv)
    return result[1:]
