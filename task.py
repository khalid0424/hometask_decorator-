from enum import Enum

class Holat(Enum):
    KHUB= 1
    BAD = 2
    
def holati_man(status: Holat):
    if status == Holat.KHUB:
        return "zurrrrrrrrrrrrrrrrrr!"
    elif status == Holat.BAD:
        return "badammmmmmmmmmmmmmm."
    else:
        return "khatogii."

print(holati_man(Holat.KHUB))  
print(holati_man(Holat.BAD)) 
