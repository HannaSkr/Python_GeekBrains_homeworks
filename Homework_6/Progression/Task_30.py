"""Задача 30: Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""


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
            
            
def get_positive_number():  #получение числа с консоли и проверка на число
    while True:
        n = (input("введите число:  "))
        try:
            if int(n) > 0: return int(n)
            elif int(n) == 0: print("вы уверены? попробуйте еще раз и введите число больше 0: ")
            else: print("число  не может быть отрицательным! попробуйте еще раз: ")
        except ValueError:    
            print("ввели не число! попробуйте еще раз: ")            


def arif_progress():
    result = [a]
    for i in range(1, n):
        result.append(result[i-1] + d)
        i+=1
    return result  


print("введите первый элемент геометрической прогрессии: ") 
a = get_integer_number()
print("введите шаг арифметической прогрессии: ")
d = get_integer_number()
print("введите количество элементов арифметической прогрессии: ")
n = get_positive_number()
result = arif_progress()
print(*result)
