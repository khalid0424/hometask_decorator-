def my_dec(func):
    def wrapper():
     print("pesh az heloo")
     func()
     print("badi az hello ")
    return wrapper

@my_dec
def hello():
   print("Hello Wourld")

hello()
