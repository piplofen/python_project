import pprint

import datetime
import logging as log
import requests
import settings as s
import signal
import sys
import time
import utils as u
import bitrixCall as bc


# class Tee(object):
#     def __init__(self, name, mode):
#         self.file = open(name, mode)
#         self.stdout = sys.stdout
#
#     def __del__(self):
#         self.close()
#
#     def write(self, data):
#         self.stdout.write(data)
#         self.file.write(data)
#
#     def flush(self):
#         self.stdout.flush()
#         self.file.flush()
#
#     def close(self):
#         if sys.stdout is self:
#             sys.stdout = self.stdout
#         self.file.close()


# WorkingDirectory=/home/fa/finarbitr/message_queue
# ExecStart=/usr/sbin/runuser -l fa -c '/home/fa/finarbitr/message_queue/venv/bin/gunicorn --chdir /home/fa/finarbitr/message_queue app:app
# -b 0.0.0.0:8000 --threads=4 --workers=1 --reload'

# def fromDictToList():
#     listFromFile = u.openFile("queue/2023-02-07", "json")
#     for id in listFromFile["result"]["events"]:
#         listTest.append(id["EVENT_DATA"]["FIELDS"]["ID"])
#     return listTest

# вытягиваю из запроса айдишники сделок
def getID(data):  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    list = []
    try:
        if data["result"]["events"]:
            for id in data["result"]["events"]:
                list.append(id["EVENT_DATA"]["FIELDS"]["ID"])
            return list
        else:
            return False
    except Exception as e:
        # log.error(f"{e}")
        return False


# получаю ивенты
def getEvent():
    dataJson = u.openFile("settings", "json")
    if u.checkDate(dataJson["timeNewAccessToken"]):
        if u.waitQue():
            URL = f"{s.C_REST_WEB_HOOK_URL}event.offline.get.json?auth={dataJson['access_token']}&limit=100000"
            r = requests.get(URL, headers=s.HEADERS)
            deal = r.json()
            pprint.pprint(deal)
            if len(deal["result"]["events"]) == 0:
                return False
            else:
                # ВОТ ТУТ РАЗДЕЛЯТЬ ИВЕНТЫ КОТОРЫЕ ПРИШЛИ ПО EVENT_NAME
                # u.writeFile("{s.workDir}logs/BitrixUpdate/{datetime.datetime.now().date()}/{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')}",
                #                 "json", "w", deal)
                # log.info(f"Успешно записал файл {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')}.json")
                # time.sleep(1)
                # return deal  # deal
                ###
                # pprint.pprint(deal)
                # # print(len(deal["result"]["events"]))
                # # print(deal["result"]["events"][0]["EVENT_NAME"])
                #
                # try:
                #     for i in range(len(deal["result"]["events"])):
                #         if deal["result"]["events"][i]["EVENT_NAME"] == "ONCRMDEALUPDATE":
                #             print("deal")
                #             u.writeFile(
                #                 f"{s.workDir}logs/BitrixUpdate/{datetime.datetime.now().date()}/{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')}",
                #                 "json", "w", deal)
                #             log.info(
                #                 f"Успешно записал файл {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')}.json")
                #             time.sleep(1)
                #             return deal  # deal
                #         elif deal["result"]["events"][i]["EVENT_NAME"] == "ONCRMCONTACTUPDATE":
                #             print("contact")
                #         else:
                #             return False
                # except:
                #     return False
                ###
                # u.writeFile(
                #     f"{datetime.datetime.now().date()}/{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')}",
                #     "json", "w", deal)
                u.writeFile(
                    f"{s.workDir}logs/BitrixUpdate/{datetime.datetime.now().date()}/{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')}",
                    "json", "w", deal)
                # log.info(f"Успешно записал файл {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')}.json")
                time.sleep(1)
                return deal  # deal
        else:
            log.error("Ошибка в очереди")
            return False
    else:
        k = s.retryQue
        if k != 0:
            k -= 1
            u.newRequest()
            getEvent()
        else:
            log.error("Кончилось количество попыток обращения к очереди")
            return False


# бесконечный цикл получающий каждое n количесво времени ивенты
def main():
    log.info("============== Запуск сервиса ==============")
    # l.info(f"{l}")
    while True:
        # print("Я ПРИНТУЮ ЧТО ТО")
        log.debug("ТЕСТ ДЕБАГ ЛОГЕРА")
        dealId = getID(getEvent())
        if dealId:
            pass
            # bc.getdeal(dealId)  # !!! вот тут поменял должно быть getdeal !!!
            # pass  # запускается обработчик накопленной очереди
        else:
            log.info("Cписок ивентов пустой")
        time.sleep(s.handler_sleep)


# функция остановки сервиса
def off():
    log.info("Остановлено")
    time.sleep(3)
    sys.exit(1)


# выход по ctrl + z
signal.signal(signal.SIGINT, lambda *_: off())

if __name__ == "__main__":
    u.logStart()
    # sys.stdout = Tee('/var/log/backend/logstdout.log', 'a')
    # print(f"Меня так не жмакают handler.py")
    main()
