"""Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
"""

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
            
            
def get_natural_number():  #получение натурального числа с консоли и проверка на число
    while True:
        n = (input("введите натуральное число:  "))
        try:
            if int(n) > 0: 
                return int(n)
            else: 
                print("натуральное число не может быть отрицательным или равным 0! попробуйте еще раз: ")
        except ValueError:    
            print("ввели не число! попробуйте еще раз: ")


def random_list(n): #заполнение списка рандомными целыми числами
    from random import randint    
    r_numbers = []
    for i in range(n):
        r_numbers.append(randint(-50, 50)) #диапазон задан небольшим для учебных целей
    
    return r_numbers


def index_low_high(r_numbers):
    result = []
    for i in range(len(r_numbers)):
        if low == high:
            if r_numbers[i] == low:            
                result.append(i)
        elif low < high:
            if low <= r_numbers[i] < high:
                result.append(i)
        else: 
            if high <= r_numbers[i] < low:
                result.append(i)
    return result


print("задайте размер массива: ")
n = get_natural_number()
print("заполним массив числами: ")
r_numbers = random_list(n)
print(*r_numbers)
print("задайте нижнее значение искомого диапазона: ")
low = get_integer_number()
print("задайте верхнее значение искомого диапазона: ")
high = get_integer_number()
result = index_low_high(r_numbers)
if len(result) != 0:
    print("индексы элементов в массиве, попадающие в заданный интервал: ")
    print(*result)
else:
    print("в массиве нет элементов из укaзанного диапазона")     

