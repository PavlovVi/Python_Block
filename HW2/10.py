# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input())
#   count_zero = 0
#   count_one = 0
#   for i in range(n):
#       x = int(input())
#       if x == 0:
#       count_zero += 1
#   else:
#       count_one += 1
#       if count_one > count_zero:
#       print(count_zero)
#   else:
#   print(count_one)

# def flip_coins(coins):
#     heads = 0

#     tails = 0
#     for coin in coins:
#         if coin == "H":
#             heads += 1
#         else:
#             tails += 1
#     min_flips = min(heads, tails)
#     flips = 0
#     while flips < min_flips:
#         if heads > tails:
#             tails += 1
#         else:
#             heads += 1
#         flips += 1
#     return flips

n = int(input())
count_zero = 0
count_one = 0
i = 0
while i < n:
    x = int(input())
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
    if count_one > count_zero:
        print(count_zero)
        break
    i += 1
else:
    print(count_one)
