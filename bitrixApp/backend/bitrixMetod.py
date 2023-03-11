import json, logging as log, newFile as db, psycopg2, utils as u, paramsView as pv
# import newFile
#
# bd = newFile.Database()
#
# l.info(f"{bd.print('NTCN')}")

bd = db.Database()

# const
tDeal = "newnewdeal"


def obr(batch):
    global m
    log.info(f"BITRIX METOD") # 8 воронка исполнения
    for i in range(len(batch)):
        listForAdd = []
        log.info(f"{batch[i]['ID']}")
        m = bd.getDeal(int(batch[i]['ID']), tDeal)
        if not m:
            log.info("СДЕЛКИ НЕТ В БАЗЕ ПИШЕМ нОВУЮ")  # insertData(self, key, value, table):
            log.info(f"{batch[i]['ID']}")
            # print("СДЕЛКИ НЕТ В БАЗЕ ПИШЕМ нОВУЮ")
            # print(f"{batch[i]['ID']} ID добавляемой сделки")
            listForAdd.clear()
            listForAdd.append(batch[i])
            dealAdd(listForAdd)
        else:
            listForAdd.clear()
            # l.info(f'{m} СДЕЛКА ЕСТЬ В БАЗЕ')
            # l.info(f"{batch[i]['ID']}")
            # print("Сделка естьв базе")
            dealUpdate(m, batch[i])
            # print(f"{batch[i]['ID']} ID сделки которая уже есть в базе")

def dealAdd(data): # Загружаю в базу актуальные сделки из файла
    log.info("Пришел")
    params, oneMoreList = pv.getView(pv.deal)
    key = ','.join(oneMoreList)
    for i in range(len(data)):
        listForBd = []
        for y in params:
            # print(f"data[{i}]{y}", type(eval(f"data[{i}]{y}")))
            # print(type(eval(f"data[{i}]{y}")))
            # print(data[i]['ID'])
            # print(params[y], 'params')
            qz = u.convertType(eval(f"data[{i}]{y}"),params[y]) # convertType(eval(f"data['result']{item}"), params[item])
            listForBd.append(qz)
        value = u.execTuple(listForBd)

            # print(qz)
            # if qz is None:
            #     qz = ""
            #     print(y)
        #     localValue.append(qz)
        # value = tuple(localValue)
        try:
            # self.insertData(key, tuple1, "naxlebniki")
            # print("GJПОСолал")
            bd.insertData(key, value, tDeal)
            listForBd.clear()
            # t.cur.execute(f"insert into newdeal({x}) values{tuple1};")
            # print(i)
            # t.conn.commit()
        except psycopg2.Error as e:
            # print("Ошибка в вызове метода")
            log.error(f"{e}")
            # print(e)
            # print(f"Сделка с {data[i]['ID']} не зашла")
            # print(data[i]["TITLE"])

    # with open("/var/razrab/backend/ba4/TESTGOODBATCH2023-02-09 11:38:12:790297.json") as file:
    #     data = json.load(file)
    #     for i in range(len(data)):
    #         values = []
    #         for y in params:
    #             qz = u.convertType(eval(f"data[{i}]{y}"),params[y])
    #             values.append(qz)
    #         tuple1 = tuple(values)
    #         print(f"insert into deal({x}) values{tuple1};")
    #         try:
    #             t.cur.execute(f"insert into newdeal({x}) values{tuple1};")
    #             print(i)
    #             t.conn.commit()
    #         except psycopg2.Error as e:
    #             print(e)
    #             print(f"Сделка с {data[i]['ID']} не зашла")
    #             print(data[i]["TITLE"])

# UPDATE weather SET (temp_lo, temp_hi, prcp) = (temp_lo+1, temp_lo+15, DEFAULT)
#   WHERE city = 'San Francisco' AND date = '2003-07-03';

def dealUpdate(data, dataNew): # bd.insertData(key, value, tDeal)
    params, oneMoreList = pv.getView(pv.deal)
    key = ','.join(oneMoreList)
    idDeal = data[0][0]  # id в базе
    # print(dataNew)
    listForBd = []
    for y in params:
        # print(eval(f"dataNew{y}"))
        qz = u.convertType(eval(f"dataNew{y}"), params[y])
        # if qz is None:
        #     qz = "[]"
        listForBd.append(qz)
    value = u.execTuple(listForBd)
    try: # def updateData(self, key, value, table, idDeal):
        bd.updateData(key, value, tDeal, idDeal)
        listForBd.clear()
            # bd.insertData(key, value, tDeal)
    except psycopg2.Error as e:
        log.error(f"{e}")

    # idDeal = data[0][0] # id в базе
    # for key in params.keys():
    #     print(eval(f"dataNew{key}"))





# def checkDealId(id):
#     t = db.getDeal(id)



def main():
    log.info(f"МАЙН")

if __name__ == '__main__':
    main()
