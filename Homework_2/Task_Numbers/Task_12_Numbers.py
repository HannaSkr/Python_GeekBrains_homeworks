"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа."""

def get_number():  #получение числа с консоли и проверка на число
    while True:
        n = (input("введите натуральное число ≤ 1000:  "))
        try:
            if int(n) > 0 and int(n) <= 1000: return int(n)
            elif int(n) > 0 and int(n) > 1000: print("Петя, число не может быть больше 1000! попробуй еще раз: ")
            elif int(n) == 0: print("Петя, 0 - не натуральное число! попробуй еще раз: ")
            else: print("Петя, натуральное число не может быть отрицательным! попробуй еще раз: ")
        except ValueError:    
            print("Петя, ты ввел не число! попробуй еще раз: ")


b = get_number()
c = get_number()
discr = b ** 2 - 4 * c
if discr < 0: print("Петя, не дури сестре голову! нет пары чисел, удовлетворяющих твоим условиям!")
elif discr == 0: 
    x1 = b / 2
    y1 = b - b / 2
    if int(x1) == float(x1) and int(y1) == float(y1): print(f"Петя, ты загадал {x1} и {y1}")
    else: print(f"Петя, ты опять обманываешь сестру! ты загадал ненатуральные числа!")
        
else: 
    x2 = (b + discr ** 0.5) / 2
    x3 = (b - discr ** 0.5) / 2
    y2 = c / x2
    y3 = c / x3
    #print(x2, y2, x3, y3)
    if int(x2) == float(x2) and int(y2) == float(y2) and int(x3) == float(x3) and int(y3) == float(y3): 
        if x2 == y3 and y2 == x3: print(f"Петя, ты загадал: {x2} и {y2} ")
        else: print(f"Петя, ты загадал: {x2} и {y2} или {x3} и {y3}") 
    else: print(f"Петя, ты опять обманываешь сестру! ты загадал ненатуральные числа!")
        
    
        
