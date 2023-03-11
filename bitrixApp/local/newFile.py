import logging

import psycopg2, logging as log

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None
    def __init__(self):
        print("ИНИЦИАЛИЗИРУЮ серверную базу")
        if self.connection is None:
            try:
                self.conn = psycopg2.connect(
                                host="127.0.0.1",
                                port=port,
                                user=user,
                                password=password,
                                database=database
                            )
                self.cur = self.conn.cursor()
                log.info("Подключился к базе")
            except psycopg2.Error as e:
                print(e)
                log.error(f"ERROR {e}")

    def getDeal(self, id, table):
        log.info(f"{log}")

        # database()
        self.cur.execute(f"select * from {table} where idbitrix = {id};")
        result = self.cur.fetchall()
        # print(result)
        if result:
            return result
        else:
            return False

    def insertData(self, key, value, table):
        try:
            self.cur.execute(f"insert into {table}({key}) values({value});")
            # print(f"insert into {table}({key}) values{value};")
            self.conn.commit()
            log.info(f"Успешно добавил запись {value[0]}")
            print(f"Успешно добавил запись {value[0]}")
        except psycopg2.Error as e:
            print(f"не добавил {e}")
            log.error(f"{e}")

    # UPDATE films SET kind = 'Dramatic' WHERE kind = 'Drama';

    def updateData(self, key, value, table, idDeal):
        try:
            # self.cur.execute(f"update {table} set ({key}) = ({value}) where id = {idDeal};")
            print(f"update {table} set ({key})= ({value}) where id = {idDeal};")
            # self.conn.commit()
            log.info(f"Успешно обновил запись {value[0]}")
            print(f"Успешно обновил запись {value[0]}")
        except psycopg2.Error as e:
            print(f"не обновил {e}")
            logging.error(f"{e}")

    def createTable(self, data, table):
        value = "id serial NOT NULL," + "\n"
        for i in range(len(data)):
            if i+1 != len(data):
                value += f"{data[i][0]} {data[i][1]} NULL," + "\n"
            if i+1 == len(data):
                value += f"{data[i][0]} {data[i][1]} NULL"
        try:
            self.cur.execute(f"create table {table}({value})")
            self.conn.commit()
            log.info(f"Успешно добавил таблицу {table}")
            print(f"Успешно добавил таблицу {table}")
        except psycopg2.Error as e:
            print(f"не добавил таблицу {table} {e}")
            logging.error(f"не добавил таблицу {table} {e}")



# l.info("ЕЖИК")