"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k
), не превосходящие числа N."""

def get_number():  #получение числа с консоли и проверка на число
    while True:
        n = (input("введите число:  "))
        try:
            if int(n) > 0: return int(n)
            elif int(n) == 0: print("вы уверены? попробуйте еще раз и введите число больше 0: ")
            else: print("целое число не может быть отрицательным! попробуйте еще раз: ")
        except ValueError:    
            print("ввели не число! попробуйте еще раз: ")

def two_squares():
    s = []
    i = 0
    while 2 ** i <= n:                 
        s.append(2 ** i)
        i += 1       
    return s

n = get_number()
s = two_squares()
print(*s, sep = " ")