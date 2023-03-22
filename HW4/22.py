# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

import random

set1 = set([random.randint(1, 100) for i in range(n)])
set2 = set([random.randint(1, 100) for i in range(m)])

intersection = sorted(list(set1 & set2))

print("Элементы, встречающиеся в обоих множествах и без повторений, в порядке возрастания:")
print(intersection)