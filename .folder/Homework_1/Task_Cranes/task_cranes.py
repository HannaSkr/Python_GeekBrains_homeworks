"""Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и 
Сережа вместе?

Пример:

6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10

"""

a = int(input("Введите общее количество сделанных журавликов: "))
b = round(a / 6)
c = round(4 * b)
print(f"Петя и Сережа сделали каждый по {b} журавликов")
print(f"Катя сделала {c} журавликов")

