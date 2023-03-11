import psycopg2


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def __init__(self):
        print("ИНИЦИАЛИЗИРУЮ")
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
                print("Подключился к базе")
            except psycopg2.Error as e:
                print(e)

    def getName(self, id):
        self.cur.execute(f"select last_name, name, second_name from employees where idbitrix = {id}")
        res = self.cur.fetchall()
        return f"{res[0][0]} {res[0][1]} {res[0][2]}"
