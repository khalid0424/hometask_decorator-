
#2. Декоратореро нависед, ки пеш аз ва баъд аз даъвати функсия яг
#он амалро иҷро мекунад (масалан, баёнияҳои чоп).
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
