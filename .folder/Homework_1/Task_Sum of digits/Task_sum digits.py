#Найдите сумму цифр трехзначного числа.
#Пример:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)


a = int(input("Введите трехзначное число от 100 до 999: "))
digit_3 = a % 10
digit_2 = (a % 100) // 10
digit_1 = a // 100
print('Сумма цифр =', end = ' ')
print(digit_1 + digit_2 + digit_3)