import psycopg2

import newFile

db = newFile.Database()

fromB = "table1"
toB = "table2"

# id
# idbitrix
# title
# contact
# otvetstvenniy
# otvetstvenniy_fu
# nomer_dela
# link_kadr_arbitr
# partner
# region

def checkTable():
    db.cur.execute(f"select exists (select * from pg_tables where tablename = '{fromB}');")
    return db.cur.fetchall()[0][0]

def checkRepeating():
    listF = []
    listT = []
    db.cur.execute(f"select idbitrix from {fromB}")
    resultB = db.cur.fetchall()
    for item in resultB:
        listF.append(item[0])
    db.cur.execute(f"select idbitrix from {toB}")
    resultB = db.cur.fetchall()
    for item in resultB:
        listT.append(item[0]) # 33746
    for id in listT:
        if id in listF:
            listF.remove(id)
    return listF

def delRepeating(list:list):
    print(list, 0)
    if list:
        try:
            for id in list:
                db.cur.execute(f"delete from {toB} where idbitrix={id}")
                db.conn.commit()
                list.remove(id)
            print("Успешно удалил повторяющиеся элементы")
            print(list, 1)
            return list
        except psycopg2.Error as e:
            print("Чот не получилось удалить повторки")
            print(e)
    else:
        print("Повторок нет")
        print(list, 2)
        return list

def insertData(list): # 33746
    for id in list:
        db.cur.execute(f"select * from {fromB} where idbitrix = {id};")
        res = db.cur.fetchall()[0]

# def insert():
#     db.cur.execute(f"select id from {toB};")
#     resId = db.cur.fetchall()
#     # print(resId)
#     listId = []
#     for id in resId:
#         listId.append(id[0])
#     # print(listId)
#
#     db.cur.execute(f"select idbitrix from {fromB};")
#     result = db.cur.fetchall()
#     res = []
#
#     for item in result:
#         # print(item)
#         res.append(item[0])
#
#     #     res.pop(0)
#     #     db.cur.execute(f"insert into {toB}(idbitrix,title,contact,otv,otvfuzad,kadrarbitrnomerdela,kadarbitrlink,partner,regionprojitki) values{tuple(res)}")
#     #     db.conn.commit()

def renameTable():
    db.cur.execute(f"alter table {fromB} rename to {fromB}old;")
    db.conn.commit()
    return True

def main():
    if checkTable():
        print("Таблица есть")
        check = checkRepeating()
        print("Можно добавлять данные, повторок либо нет, либо они удалены")
        insertData(check)
    else:
        print("таблицы нет")
        renameTable()


#
# # insert()
#
# def povtorki():
#     db.cur.execute(f"select idbitrix from {fromB}")
#     resultF = db.cur.fetchall()
#     db.cur.execute(f"select idbitrix from {toB}")
#     resultT = db.cur.fetchall()
#
#     list = []
#     listpovtorki = []
#
#     for id1 in resultT:
#         list.append(id1[0])
#     print(len(list), 1)
#
#     for id2 in resultF:
#         # print(id2[0])
#         if id2[0] in list:
#             listpovtorki.append(id2[0])
#
#     print(len(listpovtorki), 2)
#     return listpovtorki
#
# # povtorki()
#
# def delpovtorki():
#     lists = povtorki()
#     # DELETE FROM tasks WHERE status = 'DONE' RETURNING *;
#     for id in lists:
#         print(id)
#         db.cur.execute(f"delete from {toB} where idbitrix={id}")
#         db.conn.commit()
#
# # delpovtorki()

def test():
    listTest = [2]

    # if listTest:
    #     print(123)

    listF = []
    listT = []

    db.cur.execute(f"select idbitrix from {fromB}")
    resultB = db.cur.fetchall()
    for item in resultB:
        listF.append(item[0])
    db.cur.execute(f"select idbitrix from {toB}")
    resultB = db.cur.fetchall()
    for item in resultB:
        listT.append(item[0])

    for id in listT:
        if id in listF:
            print("ЕСТЬ")

    k = 0

    if 75734 in listF:
        listF.remove(75734)
        print("ЕСТЬ")
    if 75734 in listF:
         # listF.remove(75734)
        print("ЕСТЬ2")

    # print(len(listF), listF)
    # print(len(listT), listT)

if __name__ == "__main__":
    main()
    # test()