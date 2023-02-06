"""Задача 16
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

Пример:
5
1 2 3 4 5
3
-> 1"""


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
        n = (input("введите целое число:  "))
        try:
            if int(n) == float(n): 
                return int(n)
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

n = get_natural_number()
print() #для красоты, чтобы разделить строки вывода
r_numbers = random_list(n) 
print(*r_numbers, sep = " ") #для проверки, что программа работает правильно
print() #для красоты, чтобы разделить строки вывода
print("определите, какой элемент ищем")
x = get_integer_number()
cnt_search = r_numbers.count(x)
print() #для красоты, чтобы разделить строки вывода
print(f'элемент {x} встречается {cnt_search} раз') 
print()#для красоты, чтобы разделить строки вывода