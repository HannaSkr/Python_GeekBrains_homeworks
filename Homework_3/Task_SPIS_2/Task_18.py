"""Задача 18
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

Пример:

5
1 2 3 4 5
6
-> 5 """

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

def get_integer_number():  #получение целого числа с консоли и проверка на число
    while True:
        x = (input("введите целое число:  "))
        try:
            if int(x) == float(x): 
                return int(x)
            else: 
                print("ввели не целое число! попробуйте еще раз: ")
        except ValueError:    
            print("ввели не число! попробуйте еще раз: ")

def random_list(n): #заполнение списка рандомными целыми числами
    from random import randint    
    r_numbers = []
    for i in range(n):
        r_numbers.append(randint(-10, 10)) #диапазон задан небольшим для учебных целей
    
    return r_numbers

def nearest_number(r_numbers, x):
    return min(r_numbers, key = lambda i: abs(i - x))      

n = get_natural_number()
print() #для красоты, чтобы разделить строки вывода
r_numbers = random_list(n) #для проверки, что программа работает правильно
print(*r_numbers, sep = " ")
print() #для красоты, чтобы разделить строки вывода
print("определите, близость к какому элементу ищем")
x = get_integer_number()
print(nearest_number(r_numbers, x))