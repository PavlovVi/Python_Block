# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

import random
a = random.randint(0, 100)
b = random.randint(0, 100)
def sum(a, b):
    if b == 0:
        return a
    elif b > 0:
        return sum(a + 1, b - 1)
    else:
        return sum(a - 1, b + 1)
result = sum(a, b)
print("Сумма чисел", a, "и", b, "равна", result)