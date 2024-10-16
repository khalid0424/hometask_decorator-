#1. Декоратореро нависед, ки ҳар дафъа
#ҳангоми иҷрои вазифа "Function is called"
#-ро чоп мекунад.d
def my_dec(func):
    def wrapper(*args,**awargs):
     print("Function is called")
     natija = func(*args,*awargs)
     
     
    return wrapper

@my_dec
def hello(name):
   print(f"Hello {name}janob")

hello("malim")
