# Задача 12
#  Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
# помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))

for x in range(1, 1001):
    y = S - x
    if x * y == P:
        print("Числа, которые задумал Петя: ", x, "и", y)
        break
else:
    print("Решение не найдено")