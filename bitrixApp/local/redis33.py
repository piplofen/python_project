import redis
import time


class MetaSingleton1(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton1, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# metaclass=MetaSingleton1
class Redis1(metaclass=MetaSingleton1):
    connection = None

    def __init__(self, db):
        print("ИНИЦИАЛИЗИРУЮ redis")
        if self.connection is None:
            try:
                self.r = redis.Redis(host="localhost", port=port, db=db)
                print("Подключился к редиске")
            except:
                print("Не подключился к редиске")

    def insertData(self, key, value, ttl=0):
        try:
            if ttl == 0:
                self.r.set(key, value)
            else:
                self.r.set(key, value, ttl)
        except Exception as e:
            return False


    def insertDataList(self, key, value):
        self.r.lpush(key, value)
        print("Типа добавли список")

    def checkKey(self, key):
        t = self.r.get(key)
        if t is not None:
            return t
        else:
            return False

    def checkToken(self, id1, token): # токен ключ id значение
        flag = self.getData(token)
        print(flag)
        if not flag:
            print("Челикса нет")
            self.insertData(token, id1, 120)
            # self.insertDataList(id1, token, 360)
        else:
            print("Челикс есть")


    def getData(self, token):
        print(self.r.get(token), 123)
        return self.r.get(token)