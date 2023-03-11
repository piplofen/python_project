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

    def __init__(self):
        print("ИНИЦИАЛИЗИРУЮ redis")
        if self.connection is None:
            try:
                self.r = redis.Redis(host="localhost", port=port, db=3)
                print("Подключился к редиске")
            except:
                print("Не подключился к редиске")

    def insertData(self, token, data):
        print(token)
        self.r.set(token, data, 60)
        print("Записал")

    def checkKey(self, key):
        t = self.r.get(key)
        if t is not None:
            return t
        else:
            return False


class MetaSingleton2(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton2, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# metaclass=MetaSingleton1
class Redis2(metaclass=MetaSingleton1):
    connection = None

    def __init__(self):
        print("ИНИЦИАЛИЗИРУЮ redis")
        if self.connection is None:
            try:
                self.r = redis.Redis(host="localhost", port=port, db=6)
                print("Подключился к редиске")
            except:
                print("Не подключился к редиске")

    def insertData(self, token, data):
        print(token)
        self.r.set(token, data, 60)
        print("Записал")

    def checkKey(self, key):
        t = self.r.get(key)
        if t is not None:
            return t
        else:
            return False
