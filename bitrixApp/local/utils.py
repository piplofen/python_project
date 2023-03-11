import redis33, base64, json, csv, os
from secrets import token_hex

def createToken():
    return token_hex(24)


def newToken(idmemr, mac, serial):
    print("newToken")
    token = createToken()
    red3 = redis33.Redis1(3)
    if red3.checkKey(token):
        token = createToken()
        newToken(idmemr, mac, serial)
    else:
        value = f"{str(idmemr)}@{str(mac)}@{str(serial)}"
        print(token)
        try:
            red3.insertData(token, value)
        except Exception as e:
            return False

        return token




def decoding(data):
    return base64.b64decode(data)


def checkToken():
    red = redis33.Redis1(3)

    data = "id"

    token = "token"

    red.insertData(data, token, 120)

#  записываю файлик
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