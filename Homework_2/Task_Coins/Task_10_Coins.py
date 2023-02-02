"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
"""

def get_number():  #получение числа с консоли и проверка на число
    while True:
        n = (input("введите количество монеток на столе:  "))
        try:
            if int(n) > 0: return int(n)
            elif int(n) == 0: print("вы уверены, что у вас нет монет? попробуйте еще раз и введите число больше 0: ")
            else: print("число монет не может быть отрицательным! попробуйте еще раз: ")
        except ValueError:    
            print("ввели не число! попробуйте еще раз: ")
        
def binar_list(): #заполнение списка рандомными 0 и 1
    from random import randint    
    coins = []
    for i in range(n):
        coins.append(randint(0,1))
    
    return coins

def count_turns(): #подсчет ходов
    orel = 0 #0 вверху
    reshka = 0 #1 вверху
    for i in coins:
        if i == 0: orel +=  1
        else: reshka +=  1
    if orel > reshka: print(f"лучше перевернуть монеты с решкой, кол-во ходов составит {reshka}")
    elif reshka > orel: print(f"лучше перевернуть монеты с орлом, кол-во ходов составит {orel}")
    else: print(f"не имеет значения, так как {reshka} равно {orel}")   

n = get_number()
coins = binar_list()
print(*coins)
count_turns()
