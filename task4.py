def my_dec(func):
    def wrapper(*args,**awargs):
     print("pesh az heloo")
     natija = func(*args,*awargs)
     print("badi az hello ")
     return natija
    return wrapper

@my_dec
def hello(name):
   print(f"Hello {name}janob")

hello("malim")
