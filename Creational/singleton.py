class singleton(object):
    def __new__(cls, *arg, **kwargs):
        if not hasattr (cls, "_instance"):
            cls._instance = super().__new__(cls, *arg, **kwargs)
        return cls._instance

O1 = singleton()
print("Object 1: ", O1)
O1.data = 10
