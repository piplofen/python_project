import sqlite3


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def __init__(self):
        print("ИНИЦИАЛИЗИРУЮ sqlite3")
        if self.connection is None:
            try:
                self.conn = sqlite3.connect(f"database/asf")
                self.cur = self.conn.cursor()
                print(f"Подключение к локальной базе данных прошло успешно!")
                self.cur.execute("create table if not exists auth (login integer, password text, token text, type text)")
                self.conn.commit()

            except sqlite3.Error as e:
                print(f"Произошла ошибка '{e}'")

    def firstData(self, login, password, type):
        print("sql")
        self.cur.execute("select login, password from auth;")
        res = self.cur.fetchone()
        print(res)
        try:
            print("sql try")
            if res[0] == login and password is not None:
                print("Челик уже зарегался")
                print(type)
                self.cur.execute(f"update auth set type = {type} where login = {login}")
                self.conn.commit()
        except:
            print("sql except")
            self.cur.execute(f"insert into auth(login, password, type) values({login}, '{password}', '{type}')")
            self.conn.commit()
            print("Зарегал челикса")


