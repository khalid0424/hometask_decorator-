def man_dec(func):
    def wrapper(*args,**awargs):
        print("pesh")
        func(*args ,**awargs)
        print("badi ")

    return wrapper
@man_dec
def print_sub(a,b):
    print(a*b)

print_sub(33,55)

        
