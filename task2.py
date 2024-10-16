# Рақамеро, ки рӯзҳои ҳафтаро ифода 
# мекунад, муайян кунед ва 
# функсия нависед, ки рӯзи додашуда рӯзи 
# корӣ ё истироҳат аст.
import enum
from enum import Enum
class Tatil(Enum):
    YAKSHANBE = 1
    DUSHANBE =  2
    SESHANBE =  3
    CHORSHANBE =4
    PANJSHANBE =5
    JUMA =      6
    SHANBE    = 7

def is_tatil(day):
    if Tatil.DUSHANBE.value <= day.value <= Tatil.JUMA.value:
        return "Weekday"
    elif day == Tatil.YAKSHANBE or day == Tatil.SHANBE:
        return "Weekend"
    else:
        return "Invalid day"
print(is_tatil(Tatil.DUSHANBE))
print(is_tatil(Tatil.YAKSHANBE))