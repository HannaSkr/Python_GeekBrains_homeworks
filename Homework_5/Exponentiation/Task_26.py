"""Напишите программу, которая на вход принимает два числа A и B, и возводит число А в 
целую степень B с помощью рекурсии.
Пример:
A = 3; B = 5 -> 243 (3**5)
A = 2; B = 3 -> 8"""

def get_integer_number():  #получение целого числа с консоли и проверка на число
    while True:
        n = (input("введите целое число:  "))
        try:
            if int(n) == float(n): 
                return int(n)
            else: 
                print("ввели не целое число! попробуйте еще раз: ")
        except ValueError:    
            print("ввели не число! попробуйте еще раз: ")
            
def expon_number(n, degree):
    if n == 0:
        return 0
    elif degree == 0:
        return 1
    elif degree == 1:
        return n
    elif degree < 0:
        return 1/(n * expon_number(n, -degree - 1))
    else:
        return n * expon_number(n, degree - 1)
            
print("какое число будем возводить в степень?")
n = get_integer_number()
print("в какую степень будем возводить число?")
degree = get_integer_number()
print(f"результат возведения числа {n} в степень {degree} равен {round(expon_number(n, degree), 3)}")
