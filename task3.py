def count_f(func):
    count = 0  

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функсия {func.__name__} {count} маротиба иҷро шуд")
        return func(*args, **kwargs)

    return wrapper


@count_f
def jam(a,b):
    print(a+b)

@count_f
def print_text():
    
  print("Tajikistan Ba Peshh \n UUUUUUUUAAAA")
jam(33,66)
print_text
