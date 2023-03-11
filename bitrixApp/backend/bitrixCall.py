import utils as u, settings as s, logging as log, bitrixMetod as b, requests
from fast_bitrix24 import Bitrix

webhook = s.C_REST_WEB_HOOK_URL
bb = Bitrix(webhook, respect_velocity_policy=True)

listTest = []
listBach = {}
keybach = 0

# listFromFile = u.openFile("queue/2023-02-07", "json")
# for id in listFromFile["result"]["events"]:
#     value = id["EVENT_DATA"]["FIELDS"]["ID"]
#     listTest.append(value)


# def getID(deal): # !
#     global listTest
#     for id in deal["result"]["events"]:
#         value = id["EVENT_DATA"]["FIELDS"]["ID"]
#         listTest.append(value)
#         l.info(f"Весь лист id {listTest}")
#         return listTest

metod = "crm.deal.get"


def getListBach(metod):  # !
    global listTest
    global keybach
    keybach = 0
    ll = len(listTest)  # длина списка
    listdel = []  # пустой список
    if ll >= 50:  # если длина списка больше или равна 50
        y = 50  # берем 50 итераций
    else:
        y = ll  # берем количество итераций равной длине списка
    # print(y)
    for i in range(y):  # прохожусь циклом по y
        z = listTest[i]  # элемент списка равен переменной

        listBach[keybach] = f"crm.deal.get?ID={z}"  # добавляю в словарь(ключ в глобальнйо перменной, значение из переменной в строке 28)
        listdel.append(z)  # добавляю элемент глобального списка в локальным список удаления
        keybach += 1  # прибавляю 1 к ключу

    # print("Лист бач", listBach)
    # print("Лист делит", listdel)
    for i in range(len(listdel)):  # удаляем из глобального списка эдементы которые были взяты в бач
        listTest.remove(listdel[i])  # удаляю
    # print("Тист тест", listTest)
    listdel.clear()  # очищаю локальный список на удаление
    return listBach


def getdeal(dealId):
    global listTest
    listTest = dealId
    zzz = getListBach(metod)  # вызываю функцию !

    while len(zzz) > 0:  # пока длина бача больше 0
        # print("иду за запросом")
        if len(zzz) == 1:
            call = callBitrix(zzz)
            b.obr(call)
        elif len(zzz) > 1:
            log.info("Дергаю ба4")
            batch = callBatch(zzz)  # вот тут дергаем бач
            b.obr(batch)
        # l.info(f"Вызываю CALLBATCH {zzz}")
        listBach.clear()  # очищаю бач
        zzz = getListBach(metod)  # и заново запрашиваю !

    listTest.clear()
    listBach.clear()


# tasks = [
#     {
#         'ID': d['ID'],
#         'fields': {
#             'TITLE': f'{d["ID"]} - {d["TITLE"]}'
#         }
#     }
#     for d in deals
# ]
#
# b.call('crm.deal.update', tasks)
# {0: 'crm.deal.get?ID=64018'}

def checkLen(dealId):
    log.info(f"{dealId} получил массив айдишников")
    log.info(f"{len(dealId)} длина масисва")
    if len(dealId) == 1:
        log.info("Длина массива равна 1 вызываю кал")
    elif len(dealId) > 1:
        log.info("Длина массива больше 1 вызываю ба4")


# {0: 'crm.deal.get?ID=64018'}

# contacts = b.get_by_ID(
#     'crm.deal.contact.items.get',
#     [d['ID'] for d in deals])

def callBitrix(params):
    par = params[0].split('?')
    list = []
    u.waitQue()
    result = requests.get(f"{s.C_REST_WEB_HOOK_URL}{par[0]}.json?{par[1]}")
    list.append(result.json()["result"])
    return list


def callBatch(params):
    log.info(f"Дергаю ба4")
    log.info(f"{params}")
    u.waitQue()
    result = bb.call_batch({
        'halt': 0,
        'cmd': params
    })

    # u.writeFile(f"ba4/TESTGOODBATCH{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')}", "json", "w", result)
    return result


if __name__ == '__main__':

    getdeal()
